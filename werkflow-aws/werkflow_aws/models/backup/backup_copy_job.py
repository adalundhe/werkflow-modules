from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .backup_lifecycle import BackupLifecycle
from .backup_recovery_point_creator import BackupRecoveryPointCreator


class BackupCopyJob(BaseModel):
    AccountId: StrictStr | None = None
    CopyJobId: StrictStr | None = None
    SourceBackupVaultArn: StrictStr | None = None
    SourceRecoveryPointArn: StrictStr | None = None
    DestinationBackupVaultArn: StrictStr | None = None
    DestinationVaultType: StrictStr | None = None
    DestinationVaultLockState: StrictStr | None = None
    DestinationRecoveryPointArn: StrictStr | None = None
    DestinationEncryptionKeyArn: StrictStr | None = None
    DestinationRecoveryPointLifecycle: BackupLifecycle | None = None
    ResourceArn: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    CompletionDate: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    BackupSizeInBytes: StrictInt | None = None
    IamRoleArn: StrictStr | None = None
    CreatedBy: BackupRecoveryPointCreator | None = None
    CreatedByBackupJobId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ParentJobId: StrictStr | None = None
    IsParent: StrictBool | None = None
    CompositeMemberIdentifier: StrictStr | None = None
    NumberOfChildJobs: StrictInt | None = None
    ChildJobsInState: dict[StrictStr, StrictInt] | None = None
    ResourceName: StrictStr | None = None
    MessageCategory: StrictStr | None = None
