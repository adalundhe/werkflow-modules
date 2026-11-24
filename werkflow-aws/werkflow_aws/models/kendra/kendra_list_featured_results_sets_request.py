from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KendraListFeaturedResultsSetsRequest(BaseModel):
    IndexId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
