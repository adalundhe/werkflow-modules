from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMRegisterDefaultPatchBaselineRequest(BaseModel):
    BaselineId: StrictStr
