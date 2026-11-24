from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListMonitoringAlertHistoryRequest(BaseModel):
    MonitoringScheduleName: StrictStr | None = None
    MonitoringAlertName: StrictStr | None = None
    SortBy: Literal['CreationTime', 'Status'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    StatusEquals: Literal['InAlert', 'OK'] | None = None
