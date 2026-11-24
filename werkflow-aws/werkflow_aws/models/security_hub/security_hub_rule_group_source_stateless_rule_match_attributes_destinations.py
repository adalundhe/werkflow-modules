from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubRuleGroupSourceStatelessRuleMatchAttributesDestinations(BaseModel):
    AddressDefinition: StrictStr | None = None
