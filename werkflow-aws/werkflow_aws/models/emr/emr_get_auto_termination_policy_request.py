from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRGetAutoTerminationPolicyRequest(BaseModel):
    ClusterId: StrictStr
