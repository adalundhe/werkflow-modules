from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .data_zone_filter_clause import DataZoneFilterClause
from .data_zone_search_in_item import DataZoneSearchInItem
from .data_zone_search_sort import DataZoneSearchSort


class DataZoneSearchTypesRequest(BaseModel):
    domainIdentifier: StrictStr
    searchScope: Literal['ASSET_TYPE', 'FORM_TYPE', 'LINEAGE_NODE_TYPE']
    managed: StrictBool
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    searchText: StrictStr | None = None
    searchIn: list[DataZoneSearchInItem] | None = None
    filters: DataZoneFilterClause | None = None
    sort: DataZoneSearchSort | None = None
