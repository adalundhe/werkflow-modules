from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_event_actor_summary import WAFv2EventActorSummary


class WAFv2ListEventActorsResponse(BaseModel):
    EventActors: list[WAFv2EventActorSummary] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
