from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveRejectInvitationRequest(BaseModel):
    GraphArn: StrictStr
