from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rdsdb_proxy_target import RDSDBProxyTarget


class RDSRegisterDBProxyTargetsResponse(BaseModel):
    DBProxyTargets: list[RDSDBProxyTarget] | None = None
    ResponseMetadata: dict[str, Any] | None = None
