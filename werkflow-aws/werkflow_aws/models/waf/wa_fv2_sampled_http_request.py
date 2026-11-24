from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .wa_fv2_captcha_response import WAFv2CaptchaResponse
from .wa_fv2_challenge_response import WAFv2ChallengeResponse
from .wa_fv2_http_header import WAFv2HTTPHeader
from .wa_fv2_http_request import WAFv2HTTPRequest
from .wa_fv2_label import WAFv2Label


class WAFv2SampledHTTPRequest(BaseModel):
    Request: WAFv2HTTPRequest | None = None
    Weight: StrictInt | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
    Action: StrictStr | None = None
    RuleNameWithinRuleGroup: StrictStr | None = None
    RequestHeadersInserted: list[WAFv2HTTPHeader] | None = None
    ResponseCodeSent: StrictInt | None = None
    Labels: list[WAFv2Label] | None = None
    CaptchaResponse: WAFv2CaptchaResponse | None = None
    ChallengeResponse: WAFv2ChallengeResponse | None = None
    OverriddenAction: StrictStr | None = None
