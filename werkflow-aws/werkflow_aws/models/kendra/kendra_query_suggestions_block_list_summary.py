from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class KendraQuerySuggestionsBlockListSummary(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    ItemCount: StrictInt | None = None
