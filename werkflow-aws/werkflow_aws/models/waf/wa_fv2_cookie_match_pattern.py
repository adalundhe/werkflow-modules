from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_all import WAFv2All


class WAFv2CookieMatchPattern(BaseModel):
    All: WAFv2All | None = None
    IncludedCookies: list[StrictStr] | None = None
    ExcludedCookies: list[StrictStr] | None = None
