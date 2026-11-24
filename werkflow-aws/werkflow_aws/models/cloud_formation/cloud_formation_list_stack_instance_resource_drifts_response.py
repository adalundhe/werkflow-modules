from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_stack_instance_resource_drifts_summary import CloudFormationStackInstanceResourceDriftsSummary


class CloudFormationListStackInstanceResourceDriftsResponse(BaseModel):
    Summaries: list[CloudFormationStackInstanceResourceDriftsSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
