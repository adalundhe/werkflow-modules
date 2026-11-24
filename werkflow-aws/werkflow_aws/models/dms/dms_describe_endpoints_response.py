from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_endpoint import DMSEndpoint


class DMSDescribeEndpointsResponse(BaseModel):
    Marker: StrictStr | None = None
    Endpoints: list[DMSEndpoint] | None = None
    ResponseMetadata: dict[str, Any] | None = None
