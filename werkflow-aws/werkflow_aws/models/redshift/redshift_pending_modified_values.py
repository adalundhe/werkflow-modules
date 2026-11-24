from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class RedshiftPendingModifiedValues(BaseModel):
    MasterUserPassword: StrictStr | None = None
    NodeType: StrictStr | None = None
    NumberOfNodes: StrictInt | None = None
    ClusterType: StrictStr | None = None
    ClusterVersion: StrictStr | None = None
    AutomatedSnapshotRetentionPeriod: StrictInt | None = None
    ClusterIdentifier: StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    EnhancedVpcRouting: StrictBool | None = None
    MaintenanceTrackName: StrictStr | None = None
    EncryptionType: StrictStr | None = None
