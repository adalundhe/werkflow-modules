from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_front_connection_function_summary import CloudFrontConnectionFunctionSummary


class CloudFrontCreateConnectionFunctionResponse(BaseModel):
    ConnectionFunctionSummary: CloudFrontConnectionFunctionSummary | None = None
    Location: StrictStr | None = None
    ETag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
