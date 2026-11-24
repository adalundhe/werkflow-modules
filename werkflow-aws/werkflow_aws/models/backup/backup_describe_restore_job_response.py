from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .backup_restore_job_creator import BackupRestoreJobCreator


class BackupDescribeRestoreJobResponse(BaseModel):
    AccountId: StrictStr | None = None
    RestoreJobId: StrictStr | None = None
    RecoveryPointArn: StrictStr | None = None
    SourceResourceArn: StrictStr | None = None
    BackupVaultArn: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    CompletionDate: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    PercentDone: StrictStr | None = None
    BackupSizeInBytes: StrictInt | None = None
    IamRoleArn: StrictStr | None = None
    ExpectedCompletionTimeMinutes: StrictInt | None = None
    CreatedResourceArn: StrictStr | None = None
    ResourceType: StrictStr | None = None
    RecoveryPointCreationDate: datetime.datetime | StrictStr | None = None
    CreatedBy: BackupRestoreJobCreator | None = None
    ValidationStatus: StrictStr | None = None
    ValidationStatusMessage: StrictStr | None = None
    DeletionStatus: StrictStr | None = None
    DeletionStatusMessage: StrictStr | None = None
    IsParent: StrictBool | None = None
    ParentJobId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
