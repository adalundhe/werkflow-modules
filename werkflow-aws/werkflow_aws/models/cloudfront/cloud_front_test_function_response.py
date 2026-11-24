from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_test_result import CloudFrontTestResult


class CloudFrontTestFunctionResponse(BaseModel):
    TestResult: CloudFrontTestResult | None = None
    ResponseMetadata: dict[str, Any] | None = None
