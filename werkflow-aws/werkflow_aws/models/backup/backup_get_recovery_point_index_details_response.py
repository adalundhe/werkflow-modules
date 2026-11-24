from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class BackupGetRecoveryPointIndexDetailsResponse(BaseModel):
    RecoveryPointArn: StrictStr | None = None
    BackupVaultArn: StrictStr | None = None
    SourceResourceArn: StrictStr | None = None
    IndexCreationDate: datetime.datetime | StrictStr | None = None
    IndexDeletionDate: datetime.datetime | StrictStr | None = None
    IndexCompletionDate: datetime.datetime | StrictStr | None = None
    IndexStatus: StrictStr | None = None
    IndexStatusMessage: StrictStr | None = None
    TotalItemsIndexed: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
