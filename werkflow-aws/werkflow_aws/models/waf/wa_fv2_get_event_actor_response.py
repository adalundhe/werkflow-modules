from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .wa_fv2_event_actor_detail import WAFv2EventActorDetail


class WAFv2GetEventActorResponse(BaseModel):
    EventActor: WAFv2EventActorDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
