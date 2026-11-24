from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2DeleteFirewallManagerRuleGroupsRequest(BaseModel):
    WebACLArn: StrictStr
    WebACLLockToken: StrictStr
