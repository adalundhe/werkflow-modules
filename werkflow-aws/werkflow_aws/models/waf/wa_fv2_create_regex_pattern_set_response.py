from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .wa_fv2_regex_pattern_set_summary import WAFv2RegexPatternSetSummary


class WAFv2CreateRegexPatternSetResponse(BaseModel):
    Summary: WAFv2RegexPatternSetSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
