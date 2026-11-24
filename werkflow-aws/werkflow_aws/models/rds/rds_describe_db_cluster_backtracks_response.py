from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rdsdb_cluster_backtrack import RDSDBClusterBacktrack


class RDSDescribeDBClusterBacktracksResponse(BaseModel):
    Marker: StrictStr | None = None
    DBClusterBacktracks: list[RDSDBClusterBacktrack] | None = None
    ResponseMetadata: dict[str, Any] | None = None
