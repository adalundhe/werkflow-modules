from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_regex_pattern_set_summary import WAFv2RegexPatternSetSummary


class WAFv2ListRegexPatternSetsResponse(BaseModel):
    NextMarker: StrictStr | None = None
    RegexPatternSets: list[WAFv2RegexPatternSetSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
