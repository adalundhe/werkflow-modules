from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_vpc_endpoint import OpenSearchVpcEndpoint


class OpenSearchCreateVpcEndpointResponse(BaseModel):
    VpcEndpoint: OpenSearchVpcEndpoint | None = None
    ResponseMetadata: dict[str, Any] | None = None
