from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ConnectChatContactMetrics(BaseModel):
    MultiParty: StrictBool | None = None
    TotalMessages: StrictInt | None = None
    TotalBotMessages: StrictInt | None = None
    TotalBotMessageLengthInChars: StrictInt | None = None
    ConversationCloseTimeInMillis: StrictInt | None = None
    ConversationTurnCount: StrictInt | None = None
    AgentFirstResponseTimestamp: datetime.datetime | StrictStr | None = None
    AgentFirstResponseTimeInMillis: StrictInt | None = None
