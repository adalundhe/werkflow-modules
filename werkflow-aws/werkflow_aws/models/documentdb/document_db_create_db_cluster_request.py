from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .document_db_serverless_v2_scaling_configuration import DocumentDBServerlessV2ScalingConfiguration
from .document_db_tag import DocumentDBTag


class DocumentDBCreateDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr
    Engine: StrictStr
    AvailabilityZones: list[StrictStr] | None = None
    BackupRetentionPeriod: StrictInt | None = None
    DBClusterParameterGroupName: StrictStr | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    DBSubnetGroupName: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    Port: StrictInt | None = None
    MasterUsername: StrictStr | None = None
    MasterUserPassword: StrictStr | None = None
    PreferredBackupWindow: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    Tags: list[DocumentDBTag] | None = None
    StorageEncrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    PreSignedUrl: StrictStr | None = None
    EnableCloudwatchLogsExports: list[StrictStr] | None = None
    DeletionProtection: StrictBool | None = None
    GlobalClusterIdentifier: StrictStr | None = None
    StorageType: StrictStr | None = None
    ServerlessV2ScalingConfiguration: DocumentDBServerlessV2ScalingConfiguration | None = None
    ManageMasterUserPassword: StrictBool | None = None
    MasterUserSecretKmsKeyId: StrictStr | None = None
    NetworkType: StrictStr | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    SourceRegion: StrictStr | None = None
