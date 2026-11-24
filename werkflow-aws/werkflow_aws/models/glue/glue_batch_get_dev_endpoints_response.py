from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_dev_endpoint import GlueDevEndpoint


class GlueBatchGetDevEndpointsResponse(BaseModel):
    DevEndpoints: list[GlueDevEndpoint] | None = None
    DevEndpointsNotFound: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
