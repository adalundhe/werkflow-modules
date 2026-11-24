from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_formation_stack_resource import CloudFormationStackResource


class CloudFormationDescribeStackResourcesResponse(BaseModel):
    StackResources: list[CloudFormationStackResource] | None = None
    ResponseMetadata: dict[str, Any] | None = None
