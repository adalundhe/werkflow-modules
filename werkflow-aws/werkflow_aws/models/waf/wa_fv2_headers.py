from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_header_match_pattern import WAFv2HeaderMatchPattern


class WAFv2Headers(BaseModel):
    MatchPattern: WAFv2HeaderMatchPattern | None = None
    MatchScope: StrictStr | None = None
    OversizeHandling: StrictStr | None = None
