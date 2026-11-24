from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QBusinessListMessagesRequest(BaseModel):
    conversationId: StrictStr
    applicationId: StrictStr
    userId: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
