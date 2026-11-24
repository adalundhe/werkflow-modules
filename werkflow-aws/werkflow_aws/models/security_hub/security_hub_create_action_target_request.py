from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubCreateActionTargetRequest(BaseModel):
    Name: StrictStr
    Description: StrictStr
    Id: StrictStr
