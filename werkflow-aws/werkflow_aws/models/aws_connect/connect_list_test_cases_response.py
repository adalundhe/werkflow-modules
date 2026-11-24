from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_test_case_summary import ConnectTestCaseSummary


class ConnectListTestCasesResponse(BaseModel):
    TestCaseSummaryList: list[ConnectTestCaseSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
