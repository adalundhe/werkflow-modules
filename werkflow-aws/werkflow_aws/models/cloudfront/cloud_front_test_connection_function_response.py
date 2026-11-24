from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_connection_function_test_result import CloudFrontConnectionFunctionTestResult


class CloudFrontTestConnectionFunctionResponse(BaseModel):
    ConnectionFunctionTestResult: CloudFrontConnectionFunctionTestResult | None = None
    ResponseMetadata: dict[str, Any] | None = None
