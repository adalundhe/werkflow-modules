from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTSearchIndexRequest(BaseModel):
    queryString: StrictStr
    indexName: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    queryVersion: StrictStr | None = None
