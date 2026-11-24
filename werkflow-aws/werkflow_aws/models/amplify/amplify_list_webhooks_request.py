from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AmplifyListWebhooksRequest(BaseModel):
    appId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
