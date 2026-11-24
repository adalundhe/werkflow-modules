from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_function_summary import CloudFrontFunctionSummary


class CloudFrontPublishFunctionResponse(BaseModel):
    FunctionSummary: CloudFrontFunctionSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
