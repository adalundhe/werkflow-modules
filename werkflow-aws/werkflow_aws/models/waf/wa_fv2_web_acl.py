from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .wa_fv2_analytics_config import WAFv2AnalyticsConfig
from .wa_fv2_application_config import WAFv2ApplicationConfig
from .wa_fv2_association_config import WAFv2AssociationConfig
from .wa_fv2_captcha_config import WAFv2CaptchaConfig
from .wa_fv2_challenge_config import WAFv2ChallengeConfig
from .wa_fv2_custom_response_body import WAFv2CustomResponseBody
from .wa_fv2_data_protection_config import WAFv2DataProtectionConfig
from .wa_fv2_default_action import WAFv2DefaultAction
from .wa_fv2_firewall_manager_rule_group import WAFv2FirewallManagerRuleGroup
from .wa_fv2_monetization_config import WAFv2MonetizationConfig
from .wa_fv2_on_source_d_do_s_protection_config import WAFv2OnSourceDDoSProtectionConfig
from .wa_fv2_rule import WAFv2Rule
from .wa_fv2_visibility_config import WAFv2VisibilityConfig


class WAFv2WebACL(BaseModel):
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    ARN: StrictStr | None = None
    DefaultAction: WAFv2DefaultAction | None = None
    Description: StrictStr | None = None
    Rules: list[WAFv2Rule] | None = None
    VisibilityConfig: WAFv2VisibilityConfig | None = None
    DataProtectionConfig: WAFv2DataProtectionConfig | None = None
    Capacity: StrictInt | None = None
    PreProcessFirewallManagerRuleGroups: list[WAFv2FirewallManagerRuleGroup] | None = None
    PostProcessFirewallManagerRuleGroups: list[WAFv2FirewallManagerRuleGroup] | None = None
    ManagedByFirewallManager: StrictBool | None = None
    LabelNamespace: StrictStr | None = None
    CustomResponseBodies: dict[StrictStr, WAFv2CustomResponseBody] | None = None
    CaptchaConfig: WAFv2CaptchaConfig | None = None
    ChallengeConfig: WAFv2ChallengeConfig | None = None
    TokenDomains: list[StrictStr] | None = None
    AssociationConfig: WAFv2AssociationConfig | None = None
    RetrofittedByFirewallManager: StrictBool | None = None
    OnSourceDDoSProtectionConfig: WAFv2OnSourceDDoSProtectionConfig | None = None
    ApplicationConfig: WAFv2ApplicationConfig | None = None
    MonetizationConfig: WAFv2MonetizationConfig | None = None
    AnalyticsConfig: WAFv2AnalyticsConfig | None = None
