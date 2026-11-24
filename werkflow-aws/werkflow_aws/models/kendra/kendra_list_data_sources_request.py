from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KendraListDataSourcesRequest(BaseModel):
    IndexId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
