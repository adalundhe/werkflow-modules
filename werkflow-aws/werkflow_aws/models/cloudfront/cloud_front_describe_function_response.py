from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_function_summary import CloudFrontFunctionSummary


class CloudFrontDescribeFunctionResponse(BaseModel):
    FunctionSummary: CloudFrontFunctionSummary | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
