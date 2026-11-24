from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_delete_vpc_endpoint_detail import OpenSearchServerlessDeleteVpcEndpointDetail


class OpenSearchServerlessDeleteVpcEndpointResponse(BaseModel):
    deleteVpcEndpointDetail: OpenSearchServerlessDeleteVpcEndpointDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
