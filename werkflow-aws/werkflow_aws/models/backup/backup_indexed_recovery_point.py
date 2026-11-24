from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BackupIndexedRecoveryPoint(BaseModel):
    RecoveryPointArn: StrictStr | None = None
    SourceResourceArn: StrictStr | None = None
    IamRoleArn: StrictStr | None = None
    BackupCreationDate: datetime.datetime | StrictStr | None = None
    ResourceType: StrictStr | None = None
    IndexCreationDate: datetime.datetime | StrictStr | None = None
    IndexStatus: StrictStr | None = None
    IndexStatusMessage: StrictStr | None = None
    BackupVaultArn: StrictStr | None = None
