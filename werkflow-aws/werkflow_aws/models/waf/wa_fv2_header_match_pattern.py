from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_all import WAFv2All


class WAFv2HeaderMatchPattern(BaseModel):
    All: WAFv2All | None = None
    IncludedHeaders: list[StrictStr] | None = None
    ExcludedHeaders: list[StrictStr] | None = None
