from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_dev_endpoint import GlueDevEndpoint


class GlueGetDevEndpointResponse(BaseModel):
    DevEndpoint: GlueDevEndpoint | None = None
    ResponseMetadata: dict[str, Any] | None = None
