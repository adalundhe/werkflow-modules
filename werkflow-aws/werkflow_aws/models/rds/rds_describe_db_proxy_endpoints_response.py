from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rdsdb_proxy_endpoint import RDSDBProxyEndpoint


class RDSDescribeDBProxyEndpointsResponse(BaseModel):
    DBProxyEndpoints: list[RDSDBProxyEndpoint] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
