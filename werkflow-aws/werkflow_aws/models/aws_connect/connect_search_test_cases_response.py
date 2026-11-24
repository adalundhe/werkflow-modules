from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_test_case import ConnectTestCase


class ConnectSearchTestCasesResponse(BaseModel):
    TestCases: list[ConnectTestCase] | None = None
    NextToken: StrictStr | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
