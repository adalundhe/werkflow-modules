from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QBusinessConversation(BaseModel):
    conversationId: StrictStr | None = None
    title: StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
