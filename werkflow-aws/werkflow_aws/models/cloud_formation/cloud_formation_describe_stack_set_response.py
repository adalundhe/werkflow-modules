from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_formation_stack_set import CloudFormationStackSet


class CloudFormationDescribeStackSetResponse(BaseModel):
    StackSet: CloudFormationStackSet | None = None
    ResponseMetadata: dict[str, Any] | None = None
