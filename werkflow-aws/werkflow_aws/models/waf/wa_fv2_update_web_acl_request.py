from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .wa_fv2_analytics_config import WAFv2AnalyticsConfig
from .wa_fv2_application_config import WAFv2ApplicationConfig
from .wa_fv2_association_config import WAFv2AssociationConfig
from .wa_fv2_captcha_config import WAFv2CaptchaConfig
from .wa_fv2_challenge_config import WAFv2ChallengeConfig
from .wa_fv2_custom_response_body import WAFv2CustomResponseBody
from .wa_fv2_data_protection_config import WAFv2DataProtectionConfig
from .wa_fv2_default_action import WAFv2DefaultAction
from .wa_fv2_monetization_config import WAFv2MonetizationConfig
from .wa_fv2_on_source_d_do_s_protection_config import WAFv2OnSourceDDoSProtectionConfig
from .wa_fv2_rule import WAFv2Rule
from .wa_fv2_visibility_config import WAFv2VisibilityConfig


class WAFv2UpdateWebACLRequest(BaseModel):
    Name: StrictStr
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    Id: StrictStr
    DefaultAction: WAFv2DefaultAction
    VisibilityConfig: WAFv2VisibilityConfig
    LockToken: StrictStr
    Description: StrictStr | None = None
    Rules: list[WAFv2Rule] | None = None
    DataProtectionConfig: WAFv2DataProtectionConfig | None = None
    CustomResponseBodies: dict[StrictStr, WAFv2CustomResponseBody] | None = None
    CaptchaConfig: WAFv2CaptchaConfig | None = None
    ChallengeConfig: WAFv2ChallengeConfig | None = None
    TokenDomains: list[StrictStr] | None = None
    AssociationConfig: WAFv2AssociationConfig | None = None
    OnSourceDDoSProtectionConfig: WAFv2OnSourceDDoSProtectionConfig | None = None
    ApplicationConfig: WAFv2ApplicationConfig | None = None
    MonetizationConfig: WAFv2MonetizationConfig | None = None
    AnalyticsConfig: WAFv2AnalyticsConfig | None = None
