from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class BackupListBackupJobsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    ByResourceArn: StrictStr | None = None
    ByState: Literal['CREATED', 'PENDING', 'RUNNING', 'ABORTING', 'ABORTED', 'COMPLETED', 'FAILED', 'EXPIRED', 'PARTIAL'] | None = None
    ByBackupVaultName: StrictStr | None = None
    ByCreatedBefore: datetime.datetime | StrictStr | None = None
    ByCreatedAfter: datetime.datetime | StrictStr | None = None
    ByResourceType: StrictStr | None = None
    ByAccountId: StrictStr | None = None
    ByCompleteAfter: datetime.datetime | StrictStr | None = None
    ByCompleteBefore: datetime.datetime | StrictStr | None = None
    ByParentJobId: StrictStr | None = None
    ByMessageCategory: StrictStr | None = None
