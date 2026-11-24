from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListModelCardVersionsRequest(BaseModel):
    ModelCardName: StrictStr
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    MaxResults: StrictInt | None = None
    ModelCardStatus: Literal['Draft', 'PendingReview', 'Approved', 'Archived'] | None = None
    NextToken: StrictStr | None = None
    SortBy: Literal['Version'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
