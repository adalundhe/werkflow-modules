from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_email_address_info import ConnectEmailAddressInfo
from .connect_email_attachment import ConnectEmailAttachment
from .connect_inbound_additional_recipients import ConnectInboundAdditionalRecipients
from .connect_inbound_email_content import ConnectInboundEmailContent
from .connect_reference import ConnectReference
from .connect_segment_attribute_value import ConnectSegmentAttributeValue


class ConnectStartEmailContactRequest(BaseModel):
    InstanceId: StrictStr
    FromEmailAddress: ConnectEmailAddressInfo
    DestinationEmailAddress: StrictStr
    EmailMessage: ConnectInboundEmailContent
    Description: StrictStr | None = None
    References: dict[StrictStr, ConnectReference] | None = None
    Name: StrictStr | None = None
    AdditionalRecipients: ConnectInboundAdditionalRecipients | None = None
    Attachments: list[ConnectEmailAttachment] | None = None
    ContactFlowId: StrictStr | None = None
    RelatedContactId: StrictStr | None = None
    Attributes: dict[StrictStr, StrictStr] | None = None
    SegmentAttributes: dict[StrictStr, ConnectSegmentAttributeValue] | None = None
    ClientToken: StrictStr | None = None
