from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_model_sort_key import SageMakerModelSortKey
from .sage_maker_order_key import SageMakerOrderKey


class SageMakerListModelsRequest(BaseModel):
    SortBy: SageMakerModelSortKey | None = None
    SortOrder: SageMakerOrderKey | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NameContains: StrictStr | None = None
    CreationTimeBefore: datetime.datetime | None = None
    CreationTimeAfter: datetime.datetime | None = None
