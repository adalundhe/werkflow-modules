from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_api_pattern import WAFv2ApiPattern
from .wa_fv2_event_actor_reference import WAFv2EventActorReference
from .wa_fv2_event_timeline_entry import WAFv2EventTimelineEntry


class WAFv2ApiSecurityEventDetail(BaseModel):
    Label: StrictStr | None = None
    Category: StrictStr | None = None
    Confidence: StrictStr | None = None
    ApiPatterns: list[WAFv2ApiPattern] | None = None
    EventActors: list[WAFv2EventActorReference] | None = None
    Timeline: list[WAFv2EventTimelineEntry] | None = None
