from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_connection_function_summary import CloudFrontConnectionFunctionSummary


class CloudFrontPublishConnectionFunctionResponse(BaseModel):
    ConnectionFunctionSummary: CloudFrontConnectionFunctionSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
