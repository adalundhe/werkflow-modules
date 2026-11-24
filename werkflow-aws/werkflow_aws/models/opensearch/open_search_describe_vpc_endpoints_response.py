from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_vpc_endpoint import OpenSearchVpcEndpoint
from .open_search_vpc_endpoint_error import OpenSearchVpcEndpointError


class OpenSearchDescribeVpcEndpointsResponse(BaseModel):
    VpcEndpoints: list[OpenSearchVpcEndpoint] | None = None
    VpcEndpointErrors: list[OpenSearchVpcEndpointError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
