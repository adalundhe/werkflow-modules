from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class QuickSightUpdateIpRestrictionRequest(BaseModel):
    AwsAccountId: StrictStr
    IpRestrictionRuleMap: dict[StrictStr, StrictStr] | None = None
    VpcIdRestrictionRuleMap: dict[StrictStr, StrictStr] | None = None
    VpcEndpointIdRestrictionRuleMap: dict[StrictStr, StrictStr] | None = None
    Enabled: StrictBool | None = None
