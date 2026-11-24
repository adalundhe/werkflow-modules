from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class QuickSightDescribeIpRestrictionResponse(BaseModel):
    AwsAccountId: StrictStr | None = None
    IpRestrictionRuleMap: dict[StrictStr, StrictStr] | None = None
    VpcIdRestrictionRuleMap: dict[StrictStr, StrictStr] | None = None
    VpcEndpointIdRestrictionRuleMap: dict[StrictStr, StrictStr] | None = None
    Enabled: StrictBool | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
