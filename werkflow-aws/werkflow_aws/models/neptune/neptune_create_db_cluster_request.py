from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .neptune_serverless_v2_scaling_configuration import NeptuneServerlessV2ScalingConfiguration
from .neptune_tag import NeptuneTag


class NeptuneCreateDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr
    Engine: StrictStr
    AvailabilityZones: list[StrictStr] | None = None
    BackupRetentionPeriod: StrictInt | None = None
    CharacterSetName: StrictStr | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    DatabaseName: StrictStr | None = None
    DBClusterParameterGroupName: StrictStr | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    DBSubnetGroupName: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    Port: StrictInt | None = None
    MasterUsername: StrictStr | None = None
    MasterUserPassword: StrictStr | None = None
    OptionGroupName: StrictStr | None = None
    PreferredBackupWindow: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    ReplicationSourceIdentifier: StrictStr | None = None
    Tags: list[NeptuneTag] | None = None
    StorageEncrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    PreSignedUrl: StrictStr | None = None
    EnableIAMDatabaseAuthentication: StrictBool | None = None
    EnableCloudwatchLogsExports: list[StrictStr] | None = None
    DeletionProtection: StrictBool | None = None
    ServerlessV2ScalingConfiguration: NeptuneServerlessV2ScalingConfiguration | None = None
    GlobalClusterIdentifier: StrictStr | None = None
    StorageType: StrictStr | None = None
    NetworkType: StrictStr | None = None
    SourceRegion: StrictStr | None = None
