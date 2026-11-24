from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .backup_lifecycle import BackupLifecycle
from .backup_recovery_point_creator import BackupRecoveryPointCreator


class BackupJob(BaseModel):
    AccountId: StrictStr | None = None
    BackupJobId: StrictStr | None = None
    BackupVaultName: StrictStr | None = None
    BackupVaultArn: StrictStr | None = None
    VaultType: StrictStr | None = None
    VaultLockState: StrictStr | None = None
    RecoveryPointArn: StrictStr | None = None
    RecoveryPointLifecycle: BackupLifecycle | None = None
    EncryptionKeyArn: StrictStr | None = None
    IsEncrypted: StrictBool | None = None
    ResourceArn: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    CompletionDate: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    PercentDone: StrictStr | None = None
    BackupSizeInBytes: StrictInt | None = None
    IamRoleArn: StrictStr | None = None
    CreatedBy: BackupRecoveryPointCreator | None = None
    ExpectedCompletionDate: datetime.datetime | StrictStr | None = None
    StartBy: datetime.datetime | StrictStr | None = None
    ResourceType: StrictStr | None = None
    BytesTransferred: StrictInt | None = None
    BackupOptions: dict[StrictStr, StrictStr] | None = None
    BackupType: StrictStr | None = None
    ParentJobId: StrictStr | None = None
    IsParent: StrictBool | None = None
    ResourceName: StrictStr | None = None
    InitiationDate: datetime.datetime | StrictStr | None = None
    MessageCategory: StrictStr | None = None
