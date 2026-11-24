from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_create_vpc_endpoint_detail import OpenSearchServerlessCreateVpcEndpointDetail


class OpenSearchServerlessCreateVpcEndpointResponse(BaseModel):
    createVpcEndpointDetail: OpenSearchServerlessCreateVpcEndpointDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
