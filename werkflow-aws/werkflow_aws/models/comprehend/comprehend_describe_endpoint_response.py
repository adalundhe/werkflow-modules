from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_endpoint_properties import ComprehendEndpointProperties


class ComprehendDescribeEndpointResponse(BaseModel):
    EndpointProperties: ComprehendEndpointProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None
