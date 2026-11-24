from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connection_data import ConnectionData as _ConnectionDataType


class ConnectStartWebRTCContactResponse(BaseModel):
    ConnectionData: _ConnectionDataType | None = None
    ContactId: StrictStr | None = None
    ParticipantId: StrictStr | None = None
    ParticipantToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
