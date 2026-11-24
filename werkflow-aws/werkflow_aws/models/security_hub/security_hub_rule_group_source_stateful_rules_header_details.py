from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubRuleGroupSourceStatefulRulesHeaderDetails(BaseModel):
    Destination: StrictStr | None = None
    DestinationPort: StrictStr | None = None
    Direction: StrictStr | None = None
    Protocol: StrictStr | None = None
    Source: StrictStr | None = None
    SourcePort: StrictStr | None = None
