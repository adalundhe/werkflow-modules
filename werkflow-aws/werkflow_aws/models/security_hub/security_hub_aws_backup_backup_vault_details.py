from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_backup_backup_vault_notifications_details import SecurityHubAwsBackupBackupVaultNotificationsDetails


class SecurityHubAwsBackupBackupVaultDetails(BaseModel):
    BackupVaultArn: StrictStr | None = None
    BackupVaultName: StrictStr | None = None
    EncryptionKeyArn: StrictStr | None = None
    Notifications: SecurityHubAwsBackupBackupVaultNotificationsDetails | None = None
    AccessPolicy: StrictStr | None = None
