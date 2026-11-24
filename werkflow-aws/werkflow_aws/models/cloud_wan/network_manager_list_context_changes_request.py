from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerListContextChangesRequest(BaseModel):
    ContextStoreId: StrictStr
    FromVersionId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
