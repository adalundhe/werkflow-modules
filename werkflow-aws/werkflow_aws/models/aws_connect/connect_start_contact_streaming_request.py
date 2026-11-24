from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_chat_streaming_configuration import ConnectChatStreamingConfiguration


class ConnectStartContactStreamingRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    ChatStreamingConfiguration: ConnectChatStreamingConfiguration
    ClientToken: StrictStr
