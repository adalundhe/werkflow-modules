from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_cookie_match_pattern import WAFv2CookieMatchPattern


class WAFv2Cookies(BaseModel):
    MatchPattern: WAFv2CookieMatchPattern | None = None
    MatchScope: StrictStr | None = None
    OversizeHandling: StrictStr | None = None
