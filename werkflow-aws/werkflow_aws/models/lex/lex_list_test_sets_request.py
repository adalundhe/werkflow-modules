from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_test_set_sort_by import LexTestSetSortBy


class LexListTestSetsRequest(BaseModel):
    sortBy: LexTestSetSortBy | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
