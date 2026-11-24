from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_processing_job_status import SageMakerProcessingJobStatus
from .sage_maker_sort_by import SageMakerSortBy
from .sage_maker_sort_order import SageMakerSortOrder


class SageMakerListProcessingJobsRequest(BaseModel):
    CreationTimeAfter: datetime.datetime | None = None
    CreationTimeBefore: datetime.datetime | None = None
    LastModifiedTimeAfter: datetime.datetime | None = None
    LastModifiedTimeBefore: datetime.datetime | None = None
    NameContains: StrictStr | None = None
    StatusEquals: SageMakerProcessingJobStatus | None = None
    SortBy: SageMakerSortBy | None = None
    SortOrder: SageMakerSortOrder | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
