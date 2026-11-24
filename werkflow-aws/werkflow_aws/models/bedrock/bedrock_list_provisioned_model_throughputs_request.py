from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockListProvisionedModelThroughputsRequest(BaseModel):
    creationTimeAfter: datetime.datetime | StrictStr | None = None
    creationTimeBefore: datetime.datetime | StrictStr | None = None
    statusEquals: Literal['Creating', 'InService', 'Updating', 'Failed'] | None = None
    modelArnEquals: StrictStr | None = None
    nameContains: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    sortBy: Literal['CreationTime'] | None = None
    sortOrder: Literal['Ascending', 'Descending'] | None = None
