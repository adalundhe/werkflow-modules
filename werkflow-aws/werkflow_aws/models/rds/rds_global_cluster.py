from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .rds_failover_state import RDSFailoverState
from .rds_global_cluster_member import RDSGlobalClusterMember
from .rds_tag_model import RDSTagModel


class RDSGlobalCluster(BaseModel):
    GlobalClusterIdentifier: StrictStr | None = None
    GlobalClusterResourceId: StrictStr | None = None
    GlobalClusterArn: StrictStr | None = None
    Status: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    EngineLifecycleSupport: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    StorageEncrypted: StrictBool | None = None
    StorageEncryptionType: StrictStr | None = None
    DeletionProtection: StrictBool | None = None
    GlobalClusterMembers: list[RDSGlobalClusterMember] | None = None
    Endpoint: StrictStr | None = None
    FailoverState: RDSFailoverState | None = None
    TagList: list[RDSTagModel] | None = None
