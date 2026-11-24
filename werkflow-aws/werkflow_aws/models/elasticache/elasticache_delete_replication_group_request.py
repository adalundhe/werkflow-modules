from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ElasticacheDeleteReplicationGroupRequest(BaseModel):
    ReplicationGroupId: StrictStr
    RetainPrimaryCluster: StrictBool | None = None
    FinalSnapshotIdentifier: StrictStr | None = None
