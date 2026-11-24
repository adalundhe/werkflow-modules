from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rdsdb_proxy_target_group import RDSDBProxyTargetGroup


class RDSModifyDBProxyTargetGroupResponse(BaseModel):
    DBProxyTargetGroup: RDSDBProxyTargetGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
