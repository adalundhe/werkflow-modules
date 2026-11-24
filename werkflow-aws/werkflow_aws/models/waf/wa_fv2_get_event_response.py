from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .wa_fv2_event_detail_summary import WAFv2EventDetailSummary


class WAFv2GetEventResponse(BaseModel):
    Event: WAFv2EventDetailSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
