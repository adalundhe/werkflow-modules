from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMDeregisterPatchBaselineForPatchGroupRequest(BaseModel):
    BaselineId: StrictStr
    PatchGroup: StrictStr
