from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_regex import WAFv2Regex


class WAFv2RegexPatternSet(BaseModel):
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    ARN: StrictStr | None = None
    Description: StrictStr | None = None
    RegularExpressionList: list[WAFv2Regex] | None = None
