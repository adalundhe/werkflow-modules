from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .memory_db_shard_configuration_request import MemoryDBShardConfigurationRequest


class MemoryDBUpdateMultiRegionClusterRequest(BaseModel):
    MultiRegionClusterName: StrictStr
    NodeType: StrictStr | None = None
    Description: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    ShardConfiguration: MemoryDBShardConfigurationRequest | None = None
    MultiRegionParameterGroupName: StrictStr | None = None
    UpdateStrategy: Literal['coordinated', 'uncoordinated'] | None = None
