from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QBusinessListChatResponseConfigurationsRequest(BaseModel):
    applicationId: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
