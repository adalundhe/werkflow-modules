from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .personalize_dataset_schema_summary import PersonalizeDatasetSchemaSummary


class PersonalizeListSchemasResponse(BaseModel):
    schemas: list[PersonalizeDatasetSchemaSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
