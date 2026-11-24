from __future__ import annotations
from pydantic import BaseModel
from .connect_email_address_info import ConnectEmailAddressInfo


class ConnectInboundAdditionalRecipients(BaseModel):
    ToAddresses: list[ConnectEmailAddressInfo] | None = None
    CcAddresses: list[ConnectEmailAddressInfo] | None = None
