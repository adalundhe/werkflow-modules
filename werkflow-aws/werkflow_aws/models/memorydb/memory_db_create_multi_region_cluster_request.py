from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .memory_db_tag import MemoryDBTag


class MemoryDBCreateMultiRegionClusterRequest(BaseModel):
    MultiRegionClusterNameSuffix: StrictStr
    NodeType: StrictStr
    Description: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    MultiRegionParameterGroupName: StrictStr | None = None
    NumShards: StrictInt | None = None
    TLSEnabled: StrictBool | None = None
    Tags: list[MemoryDBTag] | None = None
