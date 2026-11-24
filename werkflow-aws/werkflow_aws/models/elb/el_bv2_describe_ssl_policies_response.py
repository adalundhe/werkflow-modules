from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .el_bv2_ssl_policy import ELBv2SslPolicy


class ELBv2DescribeSSLPoliciesResponse(BaseModel):
    SslPolicies: list[ELBv2SslPolicy] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
