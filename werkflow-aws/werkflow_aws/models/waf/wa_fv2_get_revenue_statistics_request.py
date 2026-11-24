from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .wa_fv2_monetization_filter import WAFv2MonetizationFilter
from .wa_fv2_time_window import WAFv2TimeWindow


class WAFv2GetRevenueStatisticsRequest(BaseModel):
    StatisticType: Literal['TOP_SOURCES_BY_REVENUE', 'TOP_PATHS_BY_REVENUE']
    TimeWindow: WAFv2TimeWindow
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    Currency: Literal['USDC']
    GroupBy: Literal['NAME', 'CATEGORY', 'INTENT', 'ORGANIZATION', 'WEBACL'] | None = None
    Filters: list[WAFv2MonetizationFilter] | None = None
    NextMarker: StrictStr | None = None
    Limit: StrictInt | None = None
    SortBy: Literal['REVENUE', 'PERCENTAGE', 'NAME'] | None = None
    SortOrder: Literal['ASC', 'DESC'] | None = None
