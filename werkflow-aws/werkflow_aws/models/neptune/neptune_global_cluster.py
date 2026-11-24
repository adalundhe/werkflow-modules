from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .neptune_failover_state import NeptuneFailoverState
from .neptune_global_cluster_member import NeptuneGlobalClusterMember
from .neptune_tag import NeptuneTag


class NeptuneGlobalCluster(BaseModel):
    GlobalClusterIdentifier: StrictStr | None = None
    GlobalClusterResourceId: StrictStr | None = None
    GlobalClusterArn: StrictStr | None = None
    Status: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    StorageEncrypted: StrictBool | None = None
    DeletionProtection: StrictBool | None = None
    GlobalClusterMembers: list[NeptuneGlobalClusterMember] | None = None
    FailoverState: NeptuneFailoverState | None = None
    TagList: list[NeptuneTag] | None = None
