from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_sort_by import SageMakerSortBy
from .sage_maker_sort_order import SageMakerSortOrder
from .sage_maker_training_job_status import SageMakerTrainingJobStatus
from .sage_maker_warm_pool_resource_status import SageMakerWarmPoolResourceStatus


class SageMakerListTrainingJobsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    CreationTimeAfter: datetime.datetime | None = None
    CreationTimeBefore: datetime.datetime | None = None
    LastModifiedTimeAfter: datetime.datetime | None = None
    LastModifiedTimeBefore: datetime.datetime | None = None
    NameContains: StrictStr | None = None
    StatusEquals: SageMakerTrainingJobStatus | None = None
    SortBy: SageMakerSortBy | None = None
    SortOrder: SageMakerSortOrder | None = None
    WarmPoolStatusEquals: SageMakerWarmPoolResourceStatus | None = None
    TrainingPlanArnEquals: StrictStr | None = None
