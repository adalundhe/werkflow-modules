from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_pipeline_managed_by import SageMakerPipelineManagedBy
from .sage_maker_sort_order import SageMakerSortOrder
from .sage_maker_sort_pipelines_by import SageMakerSortPipelinesBy


class SageMakerListPipelinesRequest(BaseModel):
    PipelineNamePrefix: StrictStr | None = None
    CreatedAfter: datetime.datetime | None = None
    CreatedBefore: datetime.datetime | None = None
    SortBy: SageMakerSortPipelinesBy | None = None
    SortOrder: SageMakerSortOrder | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    ManagedBy: SageMakerPipelineManagedBy | None = None
