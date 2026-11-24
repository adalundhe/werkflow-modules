from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class BackupListIndexedRecoveryPointsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SourceResourceArn: StrictStr | None = None
    CreatedBefore: datetime.datetime | StrictStr | None = None
    CreatedAfter: datetime.datetime | StrictStr | None = None
    ResourceType: StrictStr | None = None
    IndexStatus: Literal['PENDING', 'ACTIVE', 'FAILED', 'DELETING'] | None = None
