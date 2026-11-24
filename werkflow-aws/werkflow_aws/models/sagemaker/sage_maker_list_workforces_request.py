from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListWorkforcesRequest(BaseModel):
    SortBy: Literal['Name', 'CreateDate'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    NameContains: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
