from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsWafRegionalRateBasedRuleMatchPredicate(BaseModel):
    DataId: StrictStr | None = None
    Negated: StrictBool | None = None
    Type: StrictStr | None = None
