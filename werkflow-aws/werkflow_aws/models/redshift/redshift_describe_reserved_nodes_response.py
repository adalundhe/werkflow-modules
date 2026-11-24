from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_reserved_node import RedshiftReservedNode


class RedshiftDescribeReservedNodesResponse(BaseModel):
    Marker: StrictStr | None = None
    ReservedNodes: list[RedshiftReservedNode] | None = None
    ResponseMetadata: dict[str, Any] | None = None
