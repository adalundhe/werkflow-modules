from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListArtifactsRequest(BaseModel):
    SourceUri: StrictStr | None = None
    ArtifactType: StrictStr | None = None
    CreatedAfter: datetime.datetime | StrictStr | None = None
    CreatedBefore: datetime.datetime | StrictStr | None = None
    SortBy: Literal['CreationTime'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
