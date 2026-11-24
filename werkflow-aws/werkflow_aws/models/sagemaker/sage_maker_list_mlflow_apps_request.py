from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListMlflowAppsRequest(BaseModel):
    CreatedAfter: datetime.datetime | StrictStr | None = None
    CreatedBefore: datetime.datetime | StrictStr | None = None
    Status: Literal['Creating', 'Created', 'CreateFailed', 'Updating', 'Updated', 'UpdateFailed', 'Deleting', 'DeleteFailed', 'Deleted'] | None = None
    MlflowVersion: StrictStr | None = None
    DefaultForDomainId: StrictStr | None = None
    AccountDefaultStatus: Literal['ENABLED', 'DISABLED'] | None = None
    SortBy: Literal['Name', 'CreationTime', 'Status'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
