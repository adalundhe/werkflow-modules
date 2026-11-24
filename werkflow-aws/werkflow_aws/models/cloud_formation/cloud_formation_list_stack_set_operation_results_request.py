from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_formation_operation_result_filter import CloudFormationOperationResultFilter


class CloudFormationListStackSetOperationResultsRequest(BaseModel):
    StackSetName: StrictStr
    OperationId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    CallAs: Literal['SELF', 'DELEGATED_ADMIN'] | None = None
    Filters: list[CloudFormationOperationResultFilter] | None = None
