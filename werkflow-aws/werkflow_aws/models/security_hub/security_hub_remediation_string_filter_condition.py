from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubRemediationStringFilterCondition(BaseModel):
    Value: StrictStr
