from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_stack_set_operation_summary import CloudFormationStackSetOperationSummary


class CloudFormationListStackSetOperationsResponse(BaseModel):
    Summaries: list[CloudFormationStackSetOperationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
