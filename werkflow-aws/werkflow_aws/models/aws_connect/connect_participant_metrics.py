from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ConnectParticipantMetrics(BaseModel):
    ParticipantId: StrictStr | None = None
    ParticipantType: StrictStr | None = None
    ConversationAbandon: StrictBool | None = None
    MessagesSent: StrictInt | None = None
    NumResponses: StrictInt | None = None
    MessageLengthInChars: StrictInt | None = None
    TotalResponseTimeInMillis: StrictInt | None = None
    MaxResponseTimeInMillis: StrictInt | None = None
    LastMessageTimestamp: datetime.datetime | StrictStr | None = None
