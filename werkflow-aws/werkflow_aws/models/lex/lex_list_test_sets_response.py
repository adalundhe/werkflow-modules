from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_test_set_summary import LexTestSetSummary


class LexListTestSetsResponse(BaseModel):
    testSets: list[LexTestSetSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
