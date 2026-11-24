from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_regex_pattern_set import WAFv2RegexPatternSet


class WAFv2GetRegexPatternSetResponse(BaseModel):
    RegexPatternSet: WAFv2RegexPatternSet | None = None
    LockToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
