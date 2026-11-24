from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_stack_set_auto_deployment_target_summary import CloudFormationStackSetAutoDeploymentTargetSummary


class CloudFormationListStackSetAutoDeploymentTargetsResponse(BaseModel):
    Summaries: list[CloudFormationStackSetAutoDeploymentTargetSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
