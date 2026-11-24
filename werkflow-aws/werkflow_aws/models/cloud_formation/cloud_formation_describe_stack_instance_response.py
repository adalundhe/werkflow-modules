from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_formation_stack_instance import CloudFormationStackInstance


class CloudFormationDescribeStackInstanceResponse(BaseModel):
    StackInstance: CloudFormationStackInstance | None = None
    ResponseMetadata: dict[str, Any] | None = None
