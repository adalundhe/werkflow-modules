from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_formation_stack_set_operation import CloudFormationStackSetOperation


class CloudFormationDescribeStackSetOperationResponse(BaseModel):
    StackSetOperation: CloudFormationStackSetOperation | None = None
    ResponseMetadata: dict[str, Any] | None = None
