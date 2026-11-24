from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .wa_fv2_time_window import WAFv2TimeWindow


class WAFv2ListEventActorsRequest(BaseModel):
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    TimeWindow: WAFv2TimeWindow
    SortBy: Literal['EVENT_COUNT'] | None = None
    Limit: StrictInt | None = None
    NextMarker: StrictStr | None = None
