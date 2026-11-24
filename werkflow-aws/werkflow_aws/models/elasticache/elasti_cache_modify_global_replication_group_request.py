from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ElastiCacheModifyGlobalReplicationGroupRequest(BaseModel):
    GlobalReplicationGroupId: StrictStr
    ApplyImmediately: StrictBool
    CacheNodeType: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    CacheParameterGroupName: StrictStr | None = None
    GlobalReplicationGroupDescription: StrictStr | None = None
    AutomaticFailoverEnabled: StrictBool | None = None
