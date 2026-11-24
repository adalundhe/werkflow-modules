from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .wa_fv2_api_pattern import WAFv2ApiPattern


class WAFv2RelatedEvent(BaseModel):
    EventId: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    Label: StrictStr | None = None
    Category: StrictStr | None = None
    Confidence: StrictStr | None = None
    ApiPatterns: list[WAFv2ApiPattern] | None = None
