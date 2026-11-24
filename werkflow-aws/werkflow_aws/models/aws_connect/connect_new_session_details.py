from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_chat_streaming_configuration import ConnectChatStreamingConfiguration
from .connect_participant_details import ConnectParticipantDetails


class ConnectNewSessionDetails(BaseModel):
    SupportedMessagingContentTypes: list[StrictStr] | None = None
    ParticipantDetails: ConnectParticipantDetails | None = None
    Attributes: dict[StrictStr, StrictStr] | None = None
    StreamingConfiguration: ConnectChatStreamingConfiguration | None = None
