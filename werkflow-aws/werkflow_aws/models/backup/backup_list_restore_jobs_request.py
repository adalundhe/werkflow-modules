from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class BackupListRestoreJobsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    ByAccountId: StrictStr | None = None
    ByResourceType: StrictStr | None = None
    ByCreatedBefore: datetime.datetime | StrictStr | None = None
    ByCreatedAfter: datetime.datetime | StrictStr | None = None
    ByStatus: Literal['PENDING', 'RUNNING', 'COMPLETED', 'ABORTED', 'FAILED'] | None = None
    ByCompleteBefore: datetime.datetime | StrictStr | None = None
    ByCompleteAfter: datetime.datetime | StrictStr | None = None
    ByRestoreTestingPlanArn: StrictStr | None = None
    ByParentJobId: StrictStr | None = None
