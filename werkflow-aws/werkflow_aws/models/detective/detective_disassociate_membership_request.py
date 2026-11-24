from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveDisassociateMembershipRequest(BaseModel):
    GraphArn: StrictStr
