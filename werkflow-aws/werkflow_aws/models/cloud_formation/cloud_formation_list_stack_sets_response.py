from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_stack_set_summary import CloudFormationStackSetSummary


class CloudFormationListStackSetsResponse(BaseModel):
    Summaries: list[CloudFormationStackSetSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
