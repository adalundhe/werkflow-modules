from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .connect_email_address_info import ConnectEmailAddressInfo
from .connect_outbound_additional_recipients import ConnectOutboundAdditionalRecipients
from .connect_outbound_email_content import ConnectOutboundEmailContent
from .connect_source_campaign import ConnectSourceCampaign


class ConnectSendOutboundEmailRequest(BaseModel):
    InstanceId: StrictStr
    FromEmailAddress: ConnectEmailAddressInfo
    DestinationEmailAddress: ConnectEmailAddressInfo
    EmailMessage: ConnectOutboundEmailContent
    TrafficType: Literal['GENERAL', 'CAMPAIGN']
    AdditionalRecipients: ConnectOutboundAdditionalRecipients | None = None
    SourceCampaign: ConnectSourceCampaign | None = None
    ClientToken: StrictStr | None = None
