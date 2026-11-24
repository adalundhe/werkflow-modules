from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsWafRegionalWebAclRulesListActionDetails(BaseModel):
    Type: StrictStr | None = None
