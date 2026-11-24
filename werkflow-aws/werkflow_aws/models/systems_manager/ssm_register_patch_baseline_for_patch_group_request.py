from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMRegisterPatchBaselineForPatchGroupRequest(BaseModel):
    BaselineId: StrictStr
    PatchGroup: StrictStr
