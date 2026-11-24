from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_text_transformation import WAFv2TextTransformation


class WAFv2RateLimitQueryString(BaseModel):
    TextTransformations: list[WAFv2TextTransformation] | None = None
