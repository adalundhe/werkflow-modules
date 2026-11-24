from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QBusinessListDataSourcesRequest(BaseModel):
    applicationId: StrictStr
    indexId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
