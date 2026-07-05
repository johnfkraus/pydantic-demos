from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import dlt
from pydantic import BaseModel, ValidationError, field_validator


class Cruise(BaseModel):
    cruise_id: str
    associated_person: dict[str, Any]
    family_members: list[Any]

    @field_validator("family_members", mode="before")
    @classmethod
    def coerce_family_members(cls, v):
        if isinstance(v, dict):
            return [v]
        return v


def normalize_payload(payload: dict[str, Any]) -> dict[str, Any]:
    fixed = dict(payload)
    if isinstance(fixed.get("family_members"), dict):
        fixed["family_members"] = [fixed["family_members"]]
    return fixed


def validate_cruise(payload: dict[str, Any]) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    original_payload = payload
    corrected_payload = normalize_payload(payload)

    try:
        cruise = Cruise.model_validate(corrected_payload)
        return cruise.model_dump(), None
    except ValidationError as exc:
        error_obj = {
            "failed_json": original_payload,
            "corrected_json": corrected_payload,
            "error_text": str(exc),
            "error_count": exc.error_count(),
            "errors": exc.errors(),
        }
        return None, error_obj


def load_cruises_from_json(path: str | Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    raw = json.loads(Path(path).read_text())

    rows = raw if isinstance(raw, list) else [raw]

    valid_rows = []
    error_rows = []

    for row in rows:
        valid, error = validate_cruise(row)
        if valid is not None:
            valid_rows.append(valid)
        else:
            error_rows.append(error)

    return valid_rows, error_rows


def load_to_postgres(valid_rows: list[dict[str, Any]]):
    pipeline = dlt.pipeline(
        pipeline_name="cruises_pipeline",
        destination="postgres",
        dataset_name="cruises_dataset",
        dev_mode=True
    )

    load_info = pipeline.run(valid_rows, table_name="cruises")
    return load_info


if __name__ == "__main__":
    # valid_rows, error_rows = load_cruises_from_json("cruise_dict.json")
    valid_rows, error_rows = load_cruises_from_json("cruise_dict_fam_is_dict.json")

    with open("cruise_errors.json", "w") as f:
        json.dump(error_rows, f, indent=2, default=str)

    load_info = load_to_postgres(valid_rows)
    print(f"{load_info=}")