from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KendraListGroupsOlderThanOrderingIdRequest(BaseModel):
    IndexId: StrictStr
    OrderingId: StrictInt
    DataSourceId: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
