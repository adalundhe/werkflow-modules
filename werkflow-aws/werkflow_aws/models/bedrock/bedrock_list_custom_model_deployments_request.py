from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockListCustomModelDeploymentsRequest(BaseModel):
    createdBefore: datetime.datetime | StrictStr | None = None
    createdAfter: datetime.datetime | StrictStr | None = None
    nameContains: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    sortBy: Literal['CreationTime'] | None = None
    sortOrder: Literal['Ascending', 'Descending'] | None = None
    statusEquals: Literal['Creating', 'Active', 'Failed'] | None = None
    modelArnEquals: StrictStr | None = None
