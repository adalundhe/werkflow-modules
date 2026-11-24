from __future__ import annotations
from pydantic import BaseModel
from .connect_email_recipient import ConnectEmailRecipient


class ConnectAdditionalEmailRecipients(BaseModel):
    ToList: list[ConnectEmailRecipient] | None = None
    CcList: list[ConnectEmailRecipient] | None = None
