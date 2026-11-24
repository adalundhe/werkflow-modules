from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .wa_fv2_regex import WAFv2Regex


class WAFv2UpdateRegexPatternSetRequest(BaseModel):
    Name: StrictStr
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    Id: StrictStr
    RegularExpressionList: list[WAFv2Regex]
    LockToken: StrictStr
    Description: StrictStr | None = None
