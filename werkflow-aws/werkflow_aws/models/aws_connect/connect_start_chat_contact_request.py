from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_chat_message import ConnectChatMessage
from .connect_chat_streaming_configuration import ConnectChatStreamingConfiguration
from .connect_participant_configuration import ConnectParticipantConfiguration
from .connect_participant_details import ConnectParticipantDetails
from .connect_persistent_chat import ConnectPersistentChat
from .connect_segment_attribute_value import ConnectSegmentAttributeValue


class ConnectStartChatContactRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowId: StrictStr
    ParticipantDetails: ConnectParticipantDetails
    Attributes: dict[StrictStr, StrictStr] | None = None
    ParticipantConfiguration: ConnectParticipantConfiguration | None = None
    InitialMessage: ConnectChatMessage | None = None
    ClientToken: StrictStr | None = None
    ChatDurationInMinutes: StrictInt | None = None
    SupportedMessagingContentTypes: list[StrictStr] | None = None
    PersistentChat: ConnectPersistentChat | None = None
    RelatedContactId: StrictStr | None = None
    SegmentAttributes: dict[StrictStr, ConnectSegmentAttributeValue] | None = None
    CustomerId: StrictStr | None = None
    DisconnectOnCustomerExit: list[Literal['AGENT']] | None = None
    ConnectionTypes: list[Literal['WEBSOCKET', 'CONNECTION_CREDENTIALS', 'AUTHENTICATION_SESSION', 'WEBRTC_CONNECTION']] | None = None
    ChatStreamingConfiguration: ConnectChatStreamingConfiguration | None = None
