from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_multi_region_endpoint import SESMultiRegionEndpoint


class SESListMultiRegionEndpointsResponse(BaseModel):
    MultiRegionEndpoints: list[SESMultiRegionEndpoint] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
