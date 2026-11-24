from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_endpoint import DMSEndpoint


class DMSDeleteEndpointResponse(BaseModel):
    Endpoint: DMSEndpoint | None = None
    ResponseMetadata: dict[str, Any] | None = None
