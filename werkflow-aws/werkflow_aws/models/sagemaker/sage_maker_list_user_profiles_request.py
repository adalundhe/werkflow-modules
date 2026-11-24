from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListUserProfilesRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    SortBy: Literal['CreationTime', 'LastModifiedTime'] | None = None
    DomainIdEquals: StrictStr | None = None
    UserProfileNameContains: StrictStr | None = None
