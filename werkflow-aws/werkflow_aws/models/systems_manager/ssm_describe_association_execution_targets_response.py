from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_association_execution_target import SSMAssociationExecutionTarget


class SSMDescribeAssociationExecutionTargetsResponse(BaseModel):
    AssociationExecutionTargets: list[SSMAssociationExecutionTarget] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
