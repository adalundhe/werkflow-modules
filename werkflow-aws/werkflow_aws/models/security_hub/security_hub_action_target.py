from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubActionTarget(BaseModel):
    ActionTargetArn: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
