from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_json_match_pattern import WAFv2JsonMatchPattern


class WAFv2JsonBody(BaseModel):
    MatchPattern: WAFv2JsonMatchPattern | None = None
    MatchScope: StrictStr | None = None
    InvalidFallbackBehavior: StrictStr | None = None
    OversizeHandling: StrictStr | None = None
