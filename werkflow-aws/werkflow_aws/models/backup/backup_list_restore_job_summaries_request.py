from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class BackupListRestoreJobSummariesRequest(BaseModel):
    AccountId: StrictStr | None = None
    State: Literal['CREATED', 'PENDING', 'RUNNING', 'ABORTED', 'COMPLETED', 'FAILED', 'AGGREGATE_ALL', 'ANY'] | None = None
    ResourceType: StrictStr | None = None
    AggregationPeriod: Literal['ONE_DAY', 'SEVEN_DAYS', 'FOURTEEN_DAYS'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
