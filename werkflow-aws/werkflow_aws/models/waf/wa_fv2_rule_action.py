from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_allow_action import WAFv2AllowAction
from .wa_fv2_block_action import WAFv2BlockAction
from .wa_fv2_captcha_action import WAFv2CaptchaAction
from .wa_fv2_challenge_action import WAFv2ChallengeAction
from .wa_fv2_count_action import WAFv2CountAction
from .wa_fv2_monetize_action import WAFv2MonetizeAction


class WAFv2RuleAction(BaseModel):
    Block: WAFv2BlockAction | None = None
    Allow: WAFv2AllowAction | None = None
    Count: WAFv2CountAction | None = None
    Captcha: WAFv2CaptchaAction | None = None
    Challenge: WAFv2ChallengeAction | None = None
    Monetize: WAFv2MonetizeAction | None = None
