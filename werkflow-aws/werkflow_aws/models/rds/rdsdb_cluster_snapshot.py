from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rds_storage_encryption_type import RDSStorageEncryptionType
from .rds_tag import RDSTag


class RDSDBClusterSnapshot(BaseModel):
    AvailabilityZones: list[StrictStr] | None = None
    DBClusterSnapshotIdentifier: StrictStr | None = None
    DBClusterIdentifier: StrictStr | None = None
    SnapshotCreateTime: datetime.datetime | None = None
    Engine: StrictStr | None = None
    EngineMode: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    Status: StrictStr | None = None
    Port: StrictInt | None = None
    VpcId: StrictStr | None = None
    ClusterCreateTime: datetime.datetime | None = None
    MasterUsername: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    LicenseModel: StrictStr | None = None
    SnapshotType: StrictStr | None = None
    PercentProgress: StrictInt | None = None
    StorageEncrypted: StrictBool | None = None
    StorageEncryptionType: RDSStorageEncryptionType | None = None
    BackupRetentionPeriod: StrictInt | None = None
    PreferredBackupWindow: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    DBClusterSnapshotArn: StrictStr | None = None
    SourceDBClusterSnapshotArn: StrictStr | None = None
    IAMDatabaseAuthenticationEnabled: StrictBool | None = None
    TagList: list[RDSTag] | None = None
    StorageType: StrictStr | None = None
    StorageThroughput: StrictInt | None = None
    DbClusterResourceId: StrictStr | None = None
    DBSystemId: StrictStr | None = None
