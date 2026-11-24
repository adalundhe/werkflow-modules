from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_stack_resource_summary import CloudFormationStackResourceSummary


class CloudFormationListStackResourcesResponse(BaseModel):
    StackResourceSummaries: list[CloudFormationStackResourceSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
