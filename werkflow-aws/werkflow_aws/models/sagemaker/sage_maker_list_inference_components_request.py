from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListInferenceComponentsRequest(BaseModel):
    SortBy: Literal['Name', 'CreationTime', 'Status'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NameContains: StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    LastModifiedTimeBefore: datetime.datetime | StrictStr | None = None
    LastModifiedTimeAfter: datetime.datetime | StrictStr | None = None
    StatusEquals: Literal['InService', 'Creating', 'Updating', 'Failed', 'Deleting'] | None = None
    EndpointNameEquals: StrictStr | None = None
    VariantNameEquals: StrictStr | None = None
