from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_rds_db_cluster_snapshot_db_cluster_snapshot_attribute import SecurityHubAwsRdsDbClusterSnapshotDbClusterSnapshotAttribute


class SecurityHubAwsRdsDbClusterSnapshotDetails(BaseModel):
    AvailabilityZones: list[StrictStr] | None = None
    SnapshotCreateTime: StrictStr | None = None
    Engine: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    Status: StrictStr | None = None
    Port: StrictInt | None = None
    VpcId: StrictStr | None = None
    ClusterCreateTime: StrictStr | None = None
    MasterUsername: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    LicenseModel: StrictStr | None = None
    SnapshotType: StrictStr | None = None
    PercentProgress: StrictInt | None = None
    StorageEncrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    DbClusterIdentifier: StrictStr | None = None
    DbClusterSnapshotIdentifier: StrictStr | None = None
    IamDatabaseAuthenticationEnabled: StrictBool | None = None
    DbClusterSnapshotAttributes: list[SecurityHubAwsRdsDbClusterSnapshotDbClusterSnapshotAttribute] | None = None
