from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .document_db_failover_state import DocumentDBFailoverState
from .document_db_global_cluster_member import DocumentDBGlobalClusterMember
from .document_db_tag import DocumentDBTag


class DocumentDBGlobalCluster(BaseModel):
    GlobalClusterIdentifier: StrictStr | None = None
    GlobalClusterResourceId: StrictStr | None = None
    GlobalClusterArn: StrictStr | None = None
    Status: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    StorageEncrypted: StrictBool | None = None
    DeletionProtection: StrictBool | None = None
    GlobalClusterMembers: list[DocumentDBGlobalClusterMember] | None = None
    FailoverState: DocumentDBFailoverState | None = None
    TagList: list[DocumentDBTag] | None = None
