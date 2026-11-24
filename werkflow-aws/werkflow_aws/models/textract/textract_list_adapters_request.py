from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class TextractListAdaptersRequest(BaseModel):
    AfterCreationTime: datetime.datetime | StrictStr | None = None
    BeforeCreationTime: datetime.datetime | StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
