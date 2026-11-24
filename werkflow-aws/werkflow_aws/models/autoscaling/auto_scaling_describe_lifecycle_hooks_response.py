from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .auto_scaling_lifecycle_hook import AutoScalingLifecycleHook


class AutoScalingDescribeLifecycleHooksResponse(BaseModel):
    LifecycleHooks: list[AutoScalingLifecycleHook] | None = None
    ResponseMetadata: dict[str, Any] | None = None
