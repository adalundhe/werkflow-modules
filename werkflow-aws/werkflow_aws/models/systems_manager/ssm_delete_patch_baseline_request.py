from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMDeletePatchBaselineRequest(BaseModel):
    BaselineId: StrictStr
