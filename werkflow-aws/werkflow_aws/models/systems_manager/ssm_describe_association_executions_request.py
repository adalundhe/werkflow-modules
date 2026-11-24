from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_association_execution_filter import SSMAssociationExecutionFilter


class SSMDescribeAssociationExecutionsRequest(BaseModel):
    AssociationId: StrictStr
    Filters: list[SSMAssociationExecutionFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
