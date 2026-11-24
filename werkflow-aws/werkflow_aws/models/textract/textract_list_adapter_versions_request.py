from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class TextractListAdapterVersionsRequest(BaseModel):
    AdapterId: StrictStr | None = None
    AfterCreationTime: datetime.datetime | StrictStr | None = None
    BeforeCreationTime: datetime.datetime | StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
