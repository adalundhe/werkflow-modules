from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .emr_managed_scaling_policy import EMRManagedScalingPolicy


class EMRGetManagedScalingPolicyResponse(BaseModel):
    ManagedScalingPolicy: EMRManagedScalingPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
