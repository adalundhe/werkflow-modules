from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_rds_db_processor_feature import SecurityHubAwsRdsDbProcessorFeature


class SecurityHubAwsRdsDbSnapshotDetails(BaseModel):
    DbSnapshotIdentifier: StrictStr | None = None
    DbInstanceIdentifier: StrictStr | None = None
    SnapshotCreateTime: StrictStr | None = None
    Engine: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    Status: StrictStr | None = None
    Port: StrictInt | None = None
    AvailabilityZone: StrictStr | None = None
    VpcId: StrictStr | None = None
    InstanceCreateTime: StrictStr | None = None
    MasterUsername: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    LicenseModel: StrictStr | None = None
    SnapshotType: StrictStr | None = None
    Iops: StrictInt | None = None
    OptionGroupName: StrictStr | None = None
    PercentProgress: StrictInt | None = None
    SourceRegion: StrictStr | None = None
    SourceDbSnapshotIdentifier: StrictStr | None = None
    StorageType: StrictStr | None = None
    TdeCredentialArn: StrictStr | None = None
    Encrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    Timezone: StrictStr | None = None
    IamDatabaseAuthenticationEnabled: StrictBool | None = None
    ProcessorFeatures: list[SecurityHubAwsRdsDbProcessorFeature] | None = None
    DbiResourceId: StrictStr | None = None
