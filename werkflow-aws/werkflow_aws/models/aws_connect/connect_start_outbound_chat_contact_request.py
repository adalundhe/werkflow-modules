from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_chat_message import ConnectChatMessage
from .connect_endpoint import ConnectEndpoint
from .connect_participant_details import ConnectParticipantDetails
from .connect_segment_attribute_value import ConnectSegmentAttributeValue
from .connect_templated_message_config import ConnectTemplatedMessageConfig


class ConnectStartOutboundChatContactRequest(BaseModel):
    SourceEndpoint: ConnectEndpoint
    DestinationEndpoint: ConnectEndpoint
    InstanceId: StrictStr
    SegmentAttributes: dict[StrictStr, ConnectSegmentAttributeValue]
    ContactFlowId: StrictStr
    Attributes: dict[StrictStr, StrictStr] | None = None
    ChatDurationInMinutes: StrictInt | None = None
    ParticipantDetails: ConnectParticipantDetails | None = None
    InitialSystemMessage: ConnectChatMessage | None = None
    InitialTemplatedSystemMessage: ConnectTemplatedMessageConfig | None = None
    RelatedContactId: StrictStr | None = None
    SupportedMessagingContentTypes: list[StrictStr] | None = None
    ClientToken: StrictStr | None = None
