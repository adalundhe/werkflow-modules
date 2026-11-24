from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_search_filter_clause import GlueSearchFilterClause
from .glue_search_sort import GlueSearchSort


class GlueSearchAssetsRequest(BaseModel):
    SearchText: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Sort: GlueSearchSort | None = None
    FilterClause: GlueSearchFilterClause | None = None
