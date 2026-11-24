from __future__ import annotations
from pydantic import BaseModel
from .ssm_patch import SSMPatch
from .ssm_patch_status import SSMPatchStatus


class SSMEffectivePatch(BaseModel):
    Patch: SSMPatch | None = None
    PatchStatus: SSMPatchStatus | None = None
