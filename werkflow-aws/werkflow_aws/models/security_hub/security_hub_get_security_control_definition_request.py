from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubGetSecurityControlDefinitionRequest(BaseModel):
    SecurityControlId: StrictStr
