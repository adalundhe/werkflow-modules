from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListClustersRequest(BaseModel):
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    MaxResults: StrictInt | None = None
    NameContains: StrictStr | None = None
    NextToken: StrictStr | None = None
    SortBy: Literal['CREATION_TIME', 'NAME'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    TrainingPlanArn: StrictStr | None = None
