from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubUpdateActionTargetRequest(BaseModel):
    ActionTargetArn: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
