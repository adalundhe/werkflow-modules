from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_formation_stack_resource_detail import CloudFormationStackResourceDetail


class CloudFormationDescribeStackResourceResponse(BaseModel):
    StackResourceDetail: CloudFormationStackResourceDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
