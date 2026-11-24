from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListTrialsRequest(BaseModel):
    ExperimentName: StrictStr | None = None
    TrialComponentName: StrictStr | None = None
    CreatedAfter: datetime.datetime | StrictStr | None = None
    CreatedBefore: datetime.datetime | StrictStr | None = None
    SortBy: Literal['Name', 'CreationTime'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
