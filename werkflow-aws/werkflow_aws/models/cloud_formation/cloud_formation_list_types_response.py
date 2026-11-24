from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_type_summary import CloudFormationTypeSummary


class CloudFormationListTypesResponse(BaseModel):
    TypeSummaries: list[CloudFormationTypeSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
