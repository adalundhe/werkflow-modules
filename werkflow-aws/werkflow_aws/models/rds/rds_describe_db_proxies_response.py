from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rdsdb_proxy import RDSDBProxy


class RDSDescribeDBProxiesResponse(BaseModel):
    DBProxies: list[RDSDBProxy] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
