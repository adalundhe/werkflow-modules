from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_filter import WAFv2Filter


class WAFv2LoggingFilter(BaseModel):
    Filters: list[WAFv2Filter] | None = None
    DefaultBehavior: StrictStr | None = None
