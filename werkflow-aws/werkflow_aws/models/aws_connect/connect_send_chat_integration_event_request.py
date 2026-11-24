from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_chat_event import ConnectChatEvent
from .connect_new_session_details import ConnectNewSessionDetails


class ConnectSendChatIntegrationEventRequest(BaseModel):
    SourceId: StrictStr
    DestinationId: StrictStr
    Event: ConnectChatEvent
    Subtype: StrictStr | None = None
    NewSessionDetails: ConnectNewSessionDetails | None = None
