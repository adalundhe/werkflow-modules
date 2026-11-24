from __future__ import annotations
from pydantic import BaseModel
from .ecs_runtime_platform_override import ECSRuntimePlatformOverride


class ECSServiceRevisionOverrides(BaseModel):
    runtimePlatform: ECSRuntimePlatformOverride | None = None
