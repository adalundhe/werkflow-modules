from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class NeptuneDBClusterSnapshot(BaseModel):
    AvailabilityZones: list[StrictStr] | None = None
    DBClusterSnapshotIdentifier: StrictStr | None = None
    DBClusterIdentifier: StrictStr | None = None
    SnapshotCreateTime: datetime.datetime | StrictStr | None = None
    Engine: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    Status: StrictStr | None = None
    Port: StrictInt | None = None
    VpcId: StrictStr | None = None
    ClusterCreateTime: datetime.datetime | StrictStr | None = None
    MasterUsername: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    LicenseModel: StrictStr | None = None
    SnapshotType: StrictStr | None = None
    PercentProgress: StrictInt | None = None
    StorageEncrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    DBClusterSnapshotArn: StrictStr | None = None
    SourceDBClusterSnapshotArn: StrictStr | None = None
    IAMDatabaseAuthenticationEnabled: StrictBool | None = None
    StorageType: StrictStr | None = None
