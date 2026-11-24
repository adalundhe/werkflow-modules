from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_update_outbound_email_content import ConnectUpdateOutboundEmailContent


class ConnectUpdateOutboundEmailContactMessageRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    EmailMessage: ConnectUpdateOutboundEmailContent
