from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_test_execution_result_filter_by import LexTestExecutionResultFilterBy


class LexListTestExecutionResultItemsRequest(BaseModel):
    testExecutionId: StrictStr
    resultFilterBy: LexTestExecutionResultFilterBy
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
