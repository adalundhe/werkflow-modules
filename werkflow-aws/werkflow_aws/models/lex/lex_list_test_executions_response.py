from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_test_execution_summary import LexTestExecutionSummary


class LexListTestExecutionsResponse(BaseModel):
    testExecutions: list[LexTestExecutionSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
