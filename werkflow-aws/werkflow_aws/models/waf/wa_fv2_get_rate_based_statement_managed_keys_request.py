from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WAFv2GetRateBasedStatementManagedKeysRequest(BaseModel):
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    WebACLName: StrictStr
    WebACLId: StrictStr
    RuleName: StrictStr
    RuleGroupRuleName: StrictStr | None = None
