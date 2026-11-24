from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rdsdb_proxy_target import RDSDBProxyTarget


class RDSDescribeDBProxyTargetsResponse(BaseModel):
    Targets: list[RDSDBProxyTarget] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
