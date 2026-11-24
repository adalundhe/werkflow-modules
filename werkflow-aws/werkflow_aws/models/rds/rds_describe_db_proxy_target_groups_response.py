from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rdsdb_proxy_target_group import RDSDBProxyTargetGroup


class RDSDescribeDBProxyTargetGroupsResponse(BaseModel):
    TargetGroups: list[RDSDBProxyTargetGroup] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
