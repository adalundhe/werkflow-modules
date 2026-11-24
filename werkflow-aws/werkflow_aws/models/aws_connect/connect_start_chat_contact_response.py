from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_websocket import ConnectWebsocket
from .connection_credentials import ConnectionCredentials as _ConnectionCredentialsType


class ConnectStartChatContactResponse(BaseModel):
    ContactId: StrictStr | None = None
    ParticipantId: StrictStr | None = None
    ParticipantToken: StrictStr | None = None
    ContinuedFromContactId: StrictStr | None = None
    ConnectionCredentials: _ConnectionCredentialsType | None = None
    Websocket: ConnectWebsocket | None = None
    StreamingId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
