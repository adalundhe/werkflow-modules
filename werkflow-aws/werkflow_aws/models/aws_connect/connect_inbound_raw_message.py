from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectInboundRawMessage(BaseModel):
    Subject: StrictStr
    Body: StrictStr
    ContentType: StrictStr
    Headers: dict[Literal['REFERENCES', 'MESSAGE_ID', 'IN_REPLY_TO', 'X_SES_SPAM_VERDICT', 'X_SES_VIRUS_VERDICT'], StrictStr] | None = None
