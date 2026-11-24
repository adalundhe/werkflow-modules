from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_build_test_case import CodeBuildTestCase


class CodeBuildDescribeTestCasesResponse(BaseModel):
    nextToken: StrictStr | None = None
    testCases: list[CodeBuildTestCase] | None = None
    ResponseMetadata: dict[str, Any] | None = None
