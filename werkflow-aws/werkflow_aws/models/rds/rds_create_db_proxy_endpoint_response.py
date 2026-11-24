from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rdsdb_proxy_endpoint import RDSDBProxyEndpoint


class RDSCreateDBProxyEndpointResponse(BaseModel):
    DBProxyEndpoint: RDSDBProxyEndpoint | None = None
    ResponseMetadata: dict[str, Any] | None = None
