from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .wa_fv2_captcha_config import WAFv2CaptchaConfig
from .wa_fv2_challenge_config import WAFv2ChallengeConfig
from .wa_fv2_label import WAFv2Label
from .wa_fv2_override_action import WAFv2OverrideAction
from .wa_fv2_rule_action import WAFv2RuleAction
from .wa_fv2_statement import WAFv2Statement
from .wa_fv2_visibility_config import WAFv2VisibilityConfig


class WAFv2Rule(BaseModel):
    Name: StrictStr | None = None
    Priority: StrictInt | None = None
    Statement: WAFv2Statement | None = None
    Action: WAFv2RuleAction | None = None
    OverrideAction: WAFv2OverrideAction | None = None
    RuleLabels: list[WAFv2Label] | None = None
    VisibilityConfig: WAFv2VisibilityConfig | None = None
    CaptchaConfig: WAFv2CaptchaConfig | None = None
    ChallengeConfig: WAFv2ChallengeConfig | None = None
