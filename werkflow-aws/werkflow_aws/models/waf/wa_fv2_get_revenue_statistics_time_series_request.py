from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .wa_fv2_monetization_filter import WAFv2MonetizationFilter
from .wa_fv2_time_window import WAFv2TimeWindow


class WAFv2GetRevenueStatisticsTimeSeriesRequest(BaseModel):
    StatisticType: Literal['DATE_HISTOGRAM', 'PAYMENT_TRAFFIC']
    TimeWindow: WAFv2TimeWindow
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    Interval: Literal['MINUTELY', 'FIVE_MINUTELY', 'HOURLY', 'DAILY']
    Currency: Literal['USDC']
    GroupBy: Literal['NAME', 'CATEGORY', 'INTENT', 'ORGANIZATION', 'WEBACL'] | None = None
    Filters: list[WAFv2MonetizationFilter] | None = None
    Limit: StrictInt | None = None
    NextMarker: StrictStr | None = None
