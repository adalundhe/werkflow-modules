from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class BackupListRestoreJobsByProtectedResourceRequest(BaseModel):
    ResourceArn: StrictStr
    ByStatus: Literal['PENDING', 'RUNNING', 'COMPLETED', 'ABORTED', 'FAILED'] | None = None
    ByRecoveryPointCreationDateAfter: datetime.datetime | StrictStr | None = None
    ByRecoveryPointCreationDateBefore: datetime.datetime | StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
