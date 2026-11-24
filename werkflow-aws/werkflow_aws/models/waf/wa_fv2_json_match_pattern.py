from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_all import WAFv2All


class WAFv2JsonMatchPattern(BaseModel):
    All: WAFv2All | None = None
    IncludedPaths: list[StrictStr] | None = None
