from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .connect_inbound_raw_message import ConnectInboundRawMessage


class ConnectInboundEmailContent(BaseModel):
    MessageSourceType: Literal['RAW']
    RawMessage: ConnectInboundRawMessage | None = None
