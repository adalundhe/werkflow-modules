from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSGetViolationDetailsRequest(BaseModel):
    PolicyId: StrictStr
    MemberAccount: StrictStr
    ResourceId: StrictStr
    ResourceType: StrictStr
