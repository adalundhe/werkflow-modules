from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .rdsdb_cluster_associated_role_model import RDSDBClusterAssociatedRoleModel
from .rds_serverless_v2_scaling_configuration_model import RDSServerlessV2ScalingConfigurationModel
from .rds_tag_model import RDSTagModel
from .rds_tag_specification_model import RDSTagSpecificationModel


class RDSRestoreDBClusterFromS3Request(BaseModel):
    DBClusterIdentifier: StrictStr
    Engine: StrictStr
    MasterUsername: StrictStr
    SourceEngine: StrictStr
    SourceEngineVersion: StrictStr
    S3BucketName: StrictStr
    S3IngestionRoleArn: StrictStr
    AvailabilityZones: list[StrictStr] | None = None
    BackupRetentionPeriod: StrictInt | None = None
    CharacterSetName: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    DBClusterParameterGroupName: StrictStr | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
    DBSubnetGroupName: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    Port: StrictInt | None = None
    MasterUserPassword: StrictStr | None = None
    OptionGroupName: StrictStr | None = None
    PreferredBackupWindow: StrictStr | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    Tags: list[RDSTagModel] | None = None
    StorageEncrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    EnableIAMDatabaseAuthentication: StrictBool | None = None
    S3Prefix: StrictStr | None = None
    BacktrackWindow: StrictInt | None = None
    EnableCloudwatchLogsExports: list[StrictStr] | None = None
    DeletionProtection: StrictBool | None = None
    CopyTagsToSnapshot: StrictBool | None = None
    Domain: StrictStr | None = None
    DomainIAMRoleName: StrictStr | None = None
    StorageType: StrictStr | None = None
    NetworkType: StrictStr | None = None
    ServerlessV2ScalingConfiguration: RDSServerlessV2ScalingConfigurationModel | None = None
    ManageMasterUserPassword: StrictBool | None = None
    MasterUserSecretKmsKeyId: StrictStr | None = None
    EngineLifecycleSupport: StrictStr | None = None
    TagSpecifications: list[RDSTagSpecificationModel] | None = None
    AssociatedRoles: list[RDSDBClusterAssociatedRoleModel] | None = None
