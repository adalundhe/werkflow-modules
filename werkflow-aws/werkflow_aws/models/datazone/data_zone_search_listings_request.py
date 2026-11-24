from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .data_zone_aggregation_list_item import DataZoneAggregationListItem
from .data_zone_filter_clause import DataZoneFilterClause
from .data_zone_search_in_item import DataZoneSearchInItem
from .data_zone_search_sort import DataZoneSearchSort


class DataZoneSearchListingsRequest(BaseModel):
    domainIdentifier: StrictStr
    searchText: StrictStr | None = None
    searchIn: list[DataZoneSearchInItem] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    filters: DataZoneFilterClause | None = None
    aggregations: list[DataZoneAggregationListItem] | None = None
    sort: DataZoneSearchSort | None = None
    additionalAttributes: list[Literal['FORMS', 'TIME_SERIES_DATA_POINT_FORMS', 'TEXT_MATCH_RATIONALE']] | None = None
