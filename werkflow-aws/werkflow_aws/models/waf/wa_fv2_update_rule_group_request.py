from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .wa_fv2_custom_response_body import WAFv2CustomResponseBody
from .wa_fv2_monetization_config import WAFv2MonetizationConfig
from .wa_fv2_rule import WAFv2Rule
from .wa_fv2_visibility_config import WAFv2VisibilityConfig


class WAFv2UpdateRuleGroupRequest(BaseModel):
    Name: StrictStr
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    Id: StrictStr
    VisibilityConfig: WAFv2VisibilityConfig
    LockToken: StrictStr
    Description: StrictStr | None = None
    Rules: list[WAFv2Rule] | None = None
    CustomResponseBodies: dict[StrictStr, WAFv2CustomResponseBody] | None = None
    MonetizationConfig: WAFv2MonetizationConfig | None = None
