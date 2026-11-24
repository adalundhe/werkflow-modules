from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_vpc_endpoint_summary import OpenSearchVpcEndpointSummary


class OpenSearchDeleteVpcEndpointResponse(BaseModel):
    VpcEndpointSummary: OpenSearchVpcEndpointSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
