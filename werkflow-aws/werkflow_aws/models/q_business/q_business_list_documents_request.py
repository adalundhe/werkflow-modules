from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QBusinessListDocumentsRequest(BaseModel):
    applicationId: StrictStr
    indexId: StrictStr
    dataSourceIds: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
