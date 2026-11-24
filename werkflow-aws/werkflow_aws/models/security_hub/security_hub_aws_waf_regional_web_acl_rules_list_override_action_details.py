from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsWafRegionalWebAclRulesListOverrideActionDetails(BaseModel):
    Type: StrictStr | None = None
