from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_disconnect_reason import ConnectDisconnectReason


class ConnectStopContactRequest(BaseModel):
    ContactId: StrictStr
    InstanceId: StrictStr
    DisconnectReason: ConnectDisconnectReason | None = None
