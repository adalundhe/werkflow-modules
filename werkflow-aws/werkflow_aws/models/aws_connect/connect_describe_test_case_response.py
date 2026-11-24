from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_test_case import ConnectTestCase


class ConnectDescribeTestCaseResponse(BaseModel):
    TestCase: ConnectTestCase | None = None
    ResponseMetadata: dict[str, Any] | None = None
