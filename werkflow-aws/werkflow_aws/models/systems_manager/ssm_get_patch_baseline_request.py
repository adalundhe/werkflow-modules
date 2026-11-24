from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMGetPatchBaselineRequest(BaseModel):
    BaselineId: StrictStr
