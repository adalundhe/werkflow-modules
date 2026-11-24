from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_query_suggestions_block_list_summary import KendraQuerySuggestionsBlockListSummary


class KendraListQuerySuggestionsBlockListsResponse(BaseModel):
    BlockListSummaryItems: list[KendraQuerySuggestionsBlockListSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
