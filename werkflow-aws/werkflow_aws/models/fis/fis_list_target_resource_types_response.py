from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fis_target_resource_type_summary import FISTargetResourceTypeSummary


class FISListTargetResourceTypesResponse(BaseModel):
    targetResourceTypes: list[FISTargetResourceTypeSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
