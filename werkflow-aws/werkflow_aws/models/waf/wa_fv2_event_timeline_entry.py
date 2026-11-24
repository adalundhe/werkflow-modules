from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .wa_fv2_api_pattern import WAFv2ApiPattern


class WAFv2EventTimelineEntry(BaseModel):
    ChangeTime: datetime.datetime | StrictStr | None = None
    Label: StrictStr | None = None
    Confidence: StrictStr | None = None
    ApiPatterns: list[WAFv2ApiPattern] | None = None
