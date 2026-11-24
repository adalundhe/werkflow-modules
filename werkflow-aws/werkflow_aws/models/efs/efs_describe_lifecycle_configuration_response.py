from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .efs_lifecycle_policy import EFSLifecyclePolicy


class EFSDescribeLifecycleConfigurationResponse(BaseModel):
    LifecyclePolicies: list[EFSLifecyclePolicy] | None = None
    ResponseMetadata: dict[str, Any] | None = None
