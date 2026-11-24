from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_session_endpoint import GlueSessionEndpoint


class GlueGetSessionEndpointResponse(BaseModel):
    SparkConnect: GlueSessionEndpoint | None = None
    ResponseMetadata: dict[str, Any] | None = None
