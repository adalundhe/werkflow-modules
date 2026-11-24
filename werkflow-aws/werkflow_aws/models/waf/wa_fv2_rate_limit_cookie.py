from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_text_transformation import WAFv2TextTransformation


class WAFv2RateLimitCookie(BaseModel):
    Name: StrictStr | None = None
    TextTransformations: list[WAFv2TextTransformation] | None = None
