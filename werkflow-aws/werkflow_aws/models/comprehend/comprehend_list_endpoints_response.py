from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .comprehend_endpoint_properties import ComprehendEndpointProperties


class ComprehendListEndpointsResponse(BaseModel):
    EndpointPropertiesList: list[ComprehendEndpointProperties] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
