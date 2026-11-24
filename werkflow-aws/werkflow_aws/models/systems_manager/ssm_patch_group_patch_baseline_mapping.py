from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_patch_baseline_identity import SSMPatchBaselineIdentity


class SSMPatchGroupPatchBaselineMapping(BaseModel):
    PatchGroup: StrictStr | None = None
    BaselineIdentity: SSMPatchBaselineIdentity | None = None
