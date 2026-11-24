from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rdsdb_shard_group import RDSDBShardGroup


class RDSDescribeDBShardGroupsResponse(BaseModel):
    DBShardGroups: list[RDSDBShardGroup] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
