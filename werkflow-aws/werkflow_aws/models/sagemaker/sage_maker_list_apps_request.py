from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListAppsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    SortBy: Literal['CreationTime'] | None = None
    DomainIdEquals: StrictStr | None = None
    UserProfileNameEquals: StrictStr | None = None
    SpaceNameEquals: StrictStr | None = None
