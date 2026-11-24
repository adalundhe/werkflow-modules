from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .acme_endpoint import AcmeEndpoint as _AcmeEndpointType


class ACMDescribeAcmeEndpointResponse(BaseModel):
    AcmeEndpoint: _AcmeEndpointType | None = None
    ResponseMetadata: dict[str, Any] | None = None
