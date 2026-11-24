from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .efs_lifecycle_policy import EFSLifecyclePolicy


class EFSPutLifecycleConfigurationRequest(BaseModel):
    FileSystemId: StrictStr
    LifecyclePolicies: list[EFSLifecyclePolicy]
