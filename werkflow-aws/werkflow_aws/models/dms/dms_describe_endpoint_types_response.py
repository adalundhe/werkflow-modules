from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_supported_endpoint_type import DMSSupportedEndpointType


class DMSDescribeEndpointTypesResponse(BaseModel):
    Marker: StrictStr | None = None
    SupportedEndpointTypes: list[DMSSupportedEndpointType] | None = None
    ResponseMetadata: dict[str, Any] | None = None
