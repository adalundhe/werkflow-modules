from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_endpoint import ConnectEndpoint
from .connect_nullable_additional_recipients import ConnectNullableAdditionalRecipients
from .connect_queue_info_input import ConnectQueueInfoInput
from .connect_reference import ConnectReference
from .connect_segment_attribute_value import ConnectSegmentAttributeValue
from .connect_user_info import ConnectUserInfo


class ConnectUpdateContactRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    References: dict[StrictStr, ConnectReference] | None = None
    SegmentAttributes: dict[StrictStr, ConnectSegmentAttributeValue] | None = None
    QueueInfo: ConnectQueueInfoInput | None = None
    UserInfo: ConnectUserInfo | None = None
    CustomerEndpoint: ConnectEndpoint | None = None
    SystemEndpoint: ConnectEndpoint | None = None
    AdditionalRecipients: ConnectNullableAdditionalRecipients | None = None
