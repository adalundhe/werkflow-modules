from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .data_zone_filter_clause import DataZoneFilterClause
from .data_zone_search_in_item import DataZoneSearchInItem
from .data_zone_search_sort import DataZoneSearchSort


class DataZoneSearchRequest(BaseModel):
    domainIdentifier: StrictStr
    searchScope: Literal['ASSET', 'GLOSSARY', 'GLOSSARY_TERM', 'DATA_PRODUCT']
    owningProjectIdentifier: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    searchText: StrictStr | None = None
    searchIn: list[DataZoneSearchInItem] | None = None
    filters: DataZoneFilterClause | None = None
    sort: DataZoneSearchSort | None = None
    additionalAttributes: list[Literal['FORMS', 'TIME_SERIES_DATA_POINT_FORMS', 'TEXT_MATCH_RATIONALE']] | None = None
