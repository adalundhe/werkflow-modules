from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_email_address_info import ConnectEmailAddressInfo
from .connect_outbound_additional_recipients import ConnectOutboundAdditionalRecipients
from .connect_outbound_email_content import ConnectOutboundEmailContent


class ConnectStartOutboundEmailContactRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    DestinationEmailAddress: ConnectEmailAddressInfo
    EmailMessage: ConnectOutboundEmailContent
    FromEmailAddress: ConnectEmailAddressInfo | None = None
    AdditionalRecipients: ConnectOutboundAdditionalRecipients | None = None
    ClientToken: StrictStr | None = None
