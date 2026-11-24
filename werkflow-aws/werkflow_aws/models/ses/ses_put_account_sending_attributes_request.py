from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SESPutAccountSendingAttributesRequest(BaseModel):
    SendingEnabled: StrictBool | None = None
