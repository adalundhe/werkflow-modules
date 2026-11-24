from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .redshift_account_with_restore_access import RedshiftAccountWithRestoreAccess
from .redshift_tag import RedshiftTag


class RedshiftSnapshot(BaseModel):
    SnapshotIdentifier: StrictStr | None = None
    ClusterIdentifier: StrictStr | None = None
    SnapshotCreateTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    Port: StrictInt | None = None
    AvailabilityZone: StrictStr | None = None
    ClusterCreateTime: datetime.datetime | StrictStr | None = None
    MasterUsername: StrictStr | None = None
    ClusterVersion: StrictStr | None = None
    EngineFullVersion: StrictStr | None = None
    SnapshotType: StrictStr | None = None
    NodeType: StrictStr | None = None
    NumberOfNodes: StrictInt | None = None
    DBName: StrictStr | None = None
    VpcId: StrictStr | None = None
    Encrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    EncryptedWithHSM: StrictBool | None = None
    AccountsWithRestoreAccess: list[RedshiftAccountWithRestoreAccess] | None = None
    OwnerAccount: StrictStr | None = None
    TotalBackupSizeInMegaBytes: StrictFloat | StrictInt | None = None
    ActualIncrementalBackupSizeInMegaBytes: StrictFloat | StrictInt | None = None
    BackupProgressInMegaBytes: StrictFloat | StrictInt | None = None
    CurrentBackupRateInMegaBytesPerSecond: StrictFloat | StrictInt | None = None
    EstimatedSecondsToCompletion: StrictInt | None = None
    ElapsedTimeInSeconds: StrictInt | None = None
    SourceRegion: StrictStr | None = None
    Tags: list[RedshiftTag] | None = None
    RestorableNodeTypes: list[StrictStr] | None = None
    EnhancedVpcRouting: StrictBool | None = None
    MaintenanceTrackName: StrictStr | None = None
    ManualSnapshotRetentionPeriod: StrictInt | None = None
    ManualSnapshotRemainingDays: StrictInt | None = None
    SnapshotRetentionStartTime: datetime.datetime | StrictStr | None = None
    MasterPasswordSecretArn: StrictStr | None = None
    MasterPasswordSecretKmsKeyId: StrictStr | None = None
    SnapshotArn: StrictStr | None = None
