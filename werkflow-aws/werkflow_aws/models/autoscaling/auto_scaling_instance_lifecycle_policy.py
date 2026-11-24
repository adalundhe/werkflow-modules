from __future__ import annotations
from pydantic import BaseModel
from .auto_scaling_retention_triggers import AutoScalingRetentionTriggers


class AutoScalingInstanceLifecyclePolicy(BaseModel):
    RetentionTriggers: AutoScalingRetentionTriggers | None = None
