from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_training_plan_filter import SageMakerTrainingPlanFilter


class SageMakerListTrainingPlansRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    StartTimeAfter: datetime.datetime | StrictStr | None = None
    StartTimeBefore: datetime.datetime | StrictStr | None = None
    SortBy: Literal['TrainingPlanName', 'StartTime', 'Status'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    Filters: list[SageMakerTrainingPlanFilter] | None = None
