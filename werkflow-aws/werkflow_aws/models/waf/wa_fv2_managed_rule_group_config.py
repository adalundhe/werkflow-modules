from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_aws_managed_rules_acfp_rule_set import WAFv2AWSManagedRulesACFPRuleSet
from .wa_fv2_aws_managed_rules_ai_security_rule_set import WAFv2AWSManagedRulesAISecurityRuleSet
from .wa_fv2_aws_managed_rules_atp_rule_set import WAFv2AWSManagedRulesATPRuleSet
from .wa_fv2_aws_managed_rules_anti_d_do_s_rule_set import WAFv2AWSManagedRulesAntiDDoSRuleSet
from .wa_fv2_aws_managed_rules_bot_control_rule_set import WAFv2AWSManagedRulesBotControlRuleSet
from .wa_fv2_password_field import WAFv2PasswordField
from .wa_fv2_username_field import WAFv2UsernameField


class WAFv2ManagedRuleGroupConfig(BaseModel):
    LoginPath: StrictStr | None = None
    PayloadType: StrictStr | None = None
    UsernameField: WAFv2UsernameField | None = None
    PasswordField: WAFv2PasswordField | None = None
    AWSManagedRulesBotControlRuleSet: WAFv2AWSManagedRulesBotControlRuleSet | None = None
    AWSManagedRulesATPRuleSet: WAFv2AWSManagedRulesATPRuleSet | None = None
    AWSManagedRulesACFPRuleSet: WAFv2AWSManagedRulesACFPRuleSet | None = None
    AWSManagedRulesAntiDDoSRuleSet: WAFv2AWSManagedRulesAntiDDoSRuleSet | None = None
    AWSManagedRulesAISecurityRuleSet: WAFv2AWSManagedRulesAISecurityRuleSet | None = None
