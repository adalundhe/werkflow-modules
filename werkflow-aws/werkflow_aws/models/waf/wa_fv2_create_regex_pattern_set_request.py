from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .wa_fv2_regex import WAFv2Regex
from .wa_fv2_tag import WAFv2Tag


class WAFv2CreateRegexPatternSetRequest(BaseModel):
    Name: StrictStr
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    RegularExpressionList: list[WAFv2Regex]
    Description: StrictStr | None = None
    Tags: list[WAFv2Tag] | None = None
