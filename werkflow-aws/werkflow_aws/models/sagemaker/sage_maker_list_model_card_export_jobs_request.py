from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListModelCardExportJobsRequest(BaseModel):
    ModelCardName: StrictStr
    ModelCardVersion: StrictInt | None = None
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    ModelCardExportJobNameContains: StrictStr | None = None
    StatusEquals: Literal['InProgress', 'Completed', 'Failed'] | None = None
    SortBy: Literal['Name', 'CreationTime', 'Status'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
