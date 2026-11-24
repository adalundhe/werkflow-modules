from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .wa_fv2_custom_response_body import WAFv2CustomResponseBody
from .wa_fv2_monetization_config import WAFv2MonetizationConfig
from .wa_fv2_rule import WAFv2Rule
from .wa_fv2_tag import WAFv2Tag
from .wa_fv2_visibility_config import WAFv2VisibilityConfig


class WAFv2CreateRuleGroupRequest(BaseModel):
    Name: StrictStr
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    Capacity: StrictInt
    VisibilityConfig: WAFv2VisibilityConfig
    Description: StrictStr | None = None
    Rules: list[WAFv2Rule] | None = None
    Tags: list[WAFv2Tag] | None = None
    CustomResponseBodies: dict[StrictStr, WAFv2CustomResponseBody] | None = None
    MonetizationConfig: WAFv2MonetizationConfig | None = None
