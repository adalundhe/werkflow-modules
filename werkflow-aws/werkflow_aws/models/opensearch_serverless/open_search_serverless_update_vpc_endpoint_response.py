from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_update_vpc_endpoint_detail import OpenSearchServerlessUpdateVpcEndpointDetail


class OpenSearchServerlessUpdateVpcEndpointResponse(BaseModel):
    UpdateVpcEndpointDetail: OpenSearchServerlessUpdateVpcEndpointDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
