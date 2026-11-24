from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchListDataSourceAttachmentsRequest(BaseModel):
    id: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
