from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .neptune_availability_zone import NeptuneAvailabilityZone


class NeptuneOrderableDBInstanceOption(BaseModel):
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    DBInstanceClass: StrictStr | None = None
    LicenseModel: StrictStr | None = None
    AvailabilityZones: list[NeptuneAvailabilityZone] | None = None
    MultiAZCapable: StrictBool | None = None
    ReadReplicaCapable: StrictBool | None = None
    Vpc: StrictBool | None = None
    SupportsStorageEncryption: StrictBool | None = None
    StorageType: StrictStr | None = None
    SupportsIops: StrictBool | None = None
    SupportsEnhancedMonitoring: StrictBool | None = None
    SupportsIAMDatabaseAuthentication: StrictBool | None = None
    SupportsPerformanceInsights: StrictBool | None = None
    MinStorageSize: StrictInt | None = None
    MaxStorageSize: StrictInt | None = None
    MinIopsPerDbInstance: StrictInt | None = None
    MaxIopsPerDbInstance: StrictInt | None = None
    MinIopsPerGib: StrictFloat | StrictInt | None = None
    MaxIopsPerGib: StrictFloat | StrictInt | None = None
    SupportsGlobalDatabases: StrictBool | None = None
    SupportedNetworkTypes: list[StrictStr] | None = None
