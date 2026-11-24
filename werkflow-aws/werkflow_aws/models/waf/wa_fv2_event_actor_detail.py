from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_event_actor_change import WAFv2EventActorChange
from .wa_fv2_event_actor_detail_summary import WAFv2EventActorDetailSummary
from .wa_fv2_related_event import WAFv2RelatedEvent


class WAFv2EventActorDetail(BaseModel):
    Summary: WAFv2EventActorDetailSummary | None = None
    Events: list[WAFv2RelatedEvent] | None = None
    Changes: list[WAFv2EventActorChange] | None = None
