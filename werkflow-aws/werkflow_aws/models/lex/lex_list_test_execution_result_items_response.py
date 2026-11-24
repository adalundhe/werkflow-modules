from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_test_execution_result_items import LexTestExecutionResultItems


class LexListTestExecutionResultItemsResponse(BaseModel):
    testExecutionResults: LexTestExecutionResultItems | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
