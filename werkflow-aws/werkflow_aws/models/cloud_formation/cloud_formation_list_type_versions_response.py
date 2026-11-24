from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_type_version_summary import CloudFormationTypeVersionSummary


class CloudFormationListTypeVersionsResponse(BaseModel):
    TypeVersionSummaries: list[CloudFormationTypeVersionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
