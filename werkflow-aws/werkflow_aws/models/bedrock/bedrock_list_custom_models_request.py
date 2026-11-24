from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class BedrockListCustomModelsRequest(BaseModel):
    creationTimeBefore: datetime.datetime | StrictStr | None = None
    creationTimeAfter: datetime.datetime | StrictStr | None = None
    nameContains: StrictStr | None = None
    baseModelArnEquals: StrictStr | None = None
    foundationModelArnEquals: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    sortBy: Literal['CreationTime'] | None = None
    sortOrder: Literal['Ascending', 'Descending'] | None = None
    isOwned: StrictBool | None = None
    modelStatus: Literal['Active', 'Creating', 'Failed'] | None = None
