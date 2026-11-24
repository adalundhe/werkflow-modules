from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveAcceptInvitationRequest(BaseModel):
    GraphArn: StrictStr
