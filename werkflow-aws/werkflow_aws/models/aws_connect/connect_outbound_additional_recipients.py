from __future__ import annotations
from pydantic import BaseModel
from .connect_email_address_info import ConnectEmailAddressInfo


class ConnectOutboundAdditionalRecipients(BaseModel):
    CcEmailAddresses: list[ConnectEmailAddressInfo] | None = None
