from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SecurityHubAwsRedshiftClusterPendingModifiedValues(BaseModel):
    AutomatedSnapshotRetentionPeriod: StrictInt | None = None
    ClusterIdentifier: StrictStr | None = None
    ClusterType: StrictStr | None = None
    ClusterVersion: StrictStr | None = None
    EncryptionType: StrictStr | None = None
    EnhancedVpcRouting: StrictBool | None = None
    MaintenanceTrackName: StrictStr | None = None
    MasterUserPassword: StrictStr | None = None
    NodeType: StrictStr | None = None
    NumberOfNodes: StrictInt | None = None
    PubliclyAccessible: StrictBool | None = None
