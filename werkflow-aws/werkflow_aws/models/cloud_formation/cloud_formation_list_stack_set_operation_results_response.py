from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_stack_set_operation_result_summary import CloudFormationStackSetOperationResultSummary


class CloudFormationListStackSetOperationResultsResponse(BaseModel):
    Summaries: list[CloudFormationStackSetOperationResultSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
