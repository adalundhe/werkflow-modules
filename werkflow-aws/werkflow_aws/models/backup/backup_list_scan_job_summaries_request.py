from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class BackupListScanJobSummariesRequest(BaseModel):
    AccountId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    MalwareScanner: Literal['GUARDDUTY'] | None = None
    ScanResultStatus: Literal['NO_THREATS_FOUND', 'THREATS_FOUND', 'UNKNOWN'] | None = None
    State: Literal['CREATED', 'COMPLETED', 'COMPLETED_WITH_ISSUES', 'RUNNING', 'FAILED', 'CANCELED', 'AGGREGATE_ALL', 'ANY'] | None = None
    AggregationPeriod: Literal['ONE_DAY', 'SEVEN_DAYS', 'FOURTEEN_DAYS'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
