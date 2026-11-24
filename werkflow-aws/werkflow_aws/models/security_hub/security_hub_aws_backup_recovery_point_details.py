from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_backup_recovery_point_calculated_lifecycle_details import SecurityHubAwsBackupRecoveryPointCalculatedLifecycleDetails
from .security_hub_aws_backup_recovery_point_created_by_details import SecurityHubAwsBackupRecoveryPointCreatedByDetails
from .security_hub_aws_backup_recovery_point_lifecycle_details import SecurityHubAwsBackupRecoveryPointLifecycleDetails


class SecurityHubAwsBackupRecoveryPointDetails(BaseModel):
    BackupSizeInBytes: StrictInt | None = None
    BackupVaultArn: StrictStr | None = None
    BackupVaultName: StrictStr | None = None
    CalculatedLifecycle: SecurityHubAwsBackupRecoveryPointCalculatedLifecycleDetails | None = None
    CompletionDate: StrictStr | None = None
    CreatedBy: SecurityHubAwsBackupRecoveryPointCreatedByDetails | None = None
    CreationDate: StrictStr | None = None
    EncryptionKeyArn: StrictStr | None = None
    IamRoleArn: StrictStr | None = None
    IsEncrypted: StrictBool | None = None
    LastRestoreTime: StrictStr | None = None
    Lifecycle: SecurityHubAwsBackupRecoveryPointLifecycleDetails | None = None
    RecoveryPointArn: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    ResourceType: StrictStr | None = None
    SourceBackupVaultArn: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    StorageClass: StrictStr | None = None
