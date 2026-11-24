from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubDeleteActionTargetRequest(BaseModel):
    ActionTargetArn: StrictStr
