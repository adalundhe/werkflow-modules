from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRRemoveAutoTerminationPolicyRequest(BaseModel):
    ClusterId: StrictStr
