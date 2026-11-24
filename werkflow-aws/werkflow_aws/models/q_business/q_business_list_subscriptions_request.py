from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QBusinessListSubscriptionsRequest(BaseModel):
    applicationId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
