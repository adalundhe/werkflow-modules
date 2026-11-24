from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListHubContentsRequest(BaseModel):
    HubName: StrictStr
    HubContentType: Literal['Model', 'Notebook', 'ModelReference', 'DataSet', 'JsonDoc']
    NameContains: StrictStr | None = None
    MaxSchemaVersion: StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    SortBy: Literal['HubContentName', 'CreationTime', 'HubContentStatus'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
