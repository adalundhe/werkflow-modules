from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_stack_instance_summary import CloudFormationStackInstanceSummary


class CloudFormationListStackInstancesResponse(BaseModel):
    Summaries: list[CloudFormationStackInstanceSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
