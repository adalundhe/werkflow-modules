from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_schema_conversion_request import DMSSchemaConversionRequest


class DMSDescribeExtensionPackAssociationsResponse(BaseModel):
    Marker: StrictStr | None = None
    Requests: list[DMSSchemaConversionRequest] | None = None
    ResponseMetadata: dict[str, Any] | None = None
