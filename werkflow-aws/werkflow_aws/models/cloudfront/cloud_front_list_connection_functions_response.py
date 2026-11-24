from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_connection_function_summary import CloudFrontConnectionFunctionSummary


class CloudFrontListConnectionFunctionsResponse(BaseModel):
    NextMarker: StrictStr | None = None
    ConnectionFunctions: list[CloudFrontConnectionFunctionSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
