from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessGetPolicyRequest(BaseModel):
    applicationId: StrictStr
