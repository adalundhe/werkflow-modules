from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_association_execution_targets_filter import SSMAssociationExecutionTargetsFilter


class SSMDescribeAssociationExecutionTargetsRequest(BaseModel):
    AssociationId: StrictStr
    ExecutionId: StrictStr
    Filters: list[SSMAssociationExecutionTargetsFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
