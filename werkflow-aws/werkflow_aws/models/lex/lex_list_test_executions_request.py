from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_test_execution_sort_by import LexTestExecutionSortBy


class LexListTestExecutionsRequest(BaseModel):
    sortBy: LexTestExecutionSortBy | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
