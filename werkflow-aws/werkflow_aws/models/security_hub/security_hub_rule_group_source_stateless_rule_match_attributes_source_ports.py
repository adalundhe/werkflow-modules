from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubRuleGroupSourceStatelessRuleMatchAttributesSourcePorts(BaseModel):
    FromPort: StrictInt | None = None
    ToPort: StrictInt | None = None
