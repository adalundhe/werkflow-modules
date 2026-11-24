from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_event_detail_summary import WAFv2EventDetailSummary


class WAFv2ListEventsResponse(BaseModel):
    Events: list[WAFv2EventDetailSummary] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
