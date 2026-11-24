from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_reference import ConnectReference
from .connect_segment_attribute_value import ConnectSegmentAttributeValue
from .connect_user_info import ConnectUserInfo


class ConnectCreateContactRequest(BaseModel):
    InstanceId: StrictStr
    Channel: Literal['VOICE', 'CHAT', 'TASK', 'EMAIL']
    InitiationMethod: Literal['INBOUND', 'OUTBOUND', 'TRANSFER', 'QUEUE_TRANSFER', 'CALLBACK', 'API', 'DISCONNECT', 'MONITOR', 'EXTERNAL_OUTBOUND', 'WEBRTC_API', 'AGENT_REPLY', 'FLOW']
    ClientToken: StrictStr | None = None
    RelatedContactId: StrictStr | None = None
    Attributes: dict[StrictStr, StrictStr] | None = None
    References: dict[StrictStr, ConnectReference] | None = None
    ExpiryDurationInMinutes: StrictInt | None = None
    UserInfo: ConnectUserInfo | None = None
    InitiateAs: Literal['CONNECTED_TO_USER', 'COMPLETED'] | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    SegmentAttributes: dict[StrictStr, ConnectSegmentAttributeValue] | None = None
    PreviousContactId: StrictStr | None = None
