from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .wa_fv2_monetization_filter import WAFv2MonetizationFilter
from .wa_fv2_time_window import WAFv2TimeWindow


class WAFv2ListSettlementRecordsRequest(BaseModel):
    TimeWindow: WAFv2TimeWindow
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    Currency: Literal['USDC']
    Filters: list[WAFv2MonetizationFilter] | None = None
    SortBy: Literal['TIMESTAMP', 'AMOUNT', 'NAME', 'STATUS'] | None = None
    SortOrder: Literal['ASC', 'DESC'] | None = None
    Limit: StrictInt | None = None
    NextMarker: StrictStr | None = None
