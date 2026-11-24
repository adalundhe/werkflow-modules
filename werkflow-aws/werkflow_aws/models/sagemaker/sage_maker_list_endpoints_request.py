from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_endpoint_sort_key import SageMakerEndpointSortKey
from .sage_maker_endpoint_status import SageMakerEndpointStatus
from .sage_maker_order_key import SageMakerOrderKey


class SageMakerListEndpointsRequest(BaseModel):
    SortBy: SageMakerEndpointSortKey | None = None
    SortOrder: SageMakerOrderKey | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NameContains: StrictStr | None = None
    CreationTimeBefore: datetime.datetime | None = None
    CreationTimeAfter: datetime.datetime | None = None
    LastModifiedTimeBefore: datetime.datetime | None = None
    LastModifiedTimeAfter: datetime.datetime | None = None
    StatusEquals: SageMakerEndpointStatus | None = None
