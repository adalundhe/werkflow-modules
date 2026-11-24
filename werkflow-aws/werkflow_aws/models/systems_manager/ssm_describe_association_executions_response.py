from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_association_execution import SSMAssociationExecution


class SSMDescribeAssociationExecutionsResponse(BaseModel):
    AssociationExecutions: list[SSMAssociationExecution] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
