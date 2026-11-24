from __future__ import annotations
from pydantic import BaseModel
from .glue_search_attribute_filter import GlueSearchAttributeFilter
from .glue_search_map_filter import GlueSearchMapFilter


class GlueSearchFilterClause(BaseModel):
    AndAllFilters: list[GlueSearchFilterClause] | None = None
    OrAnyFilters: list[GlueSearchFilterClause] | None = None
    AttributeFilter: GlueSearchAttributeFilter | None = None
    MapFilter: GlueSearchMapFilter | None = None
