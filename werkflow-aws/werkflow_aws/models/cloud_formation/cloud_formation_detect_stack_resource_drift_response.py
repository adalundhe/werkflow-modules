from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_formation_stack_resource_drift import CloudFormationStackResourceDrift


class CloudFormationDetectStackResourceDriftResponse(BaseModel):
    StackResourceDrift: CloudFormationStackResourceDrift | None = None
    ResponseMetadata: dict[str, Any] | None = None
