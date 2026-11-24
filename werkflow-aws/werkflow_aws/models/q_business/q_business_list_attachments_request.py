from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QBusinessListAttachmentsRequest(BaseModel):
    applicationId: StrictStr
    conversationId: StrictStr | None = None
    userId: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
