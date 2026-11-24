from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .connect_update_outbound_raw_message import ConnectUpdateOutboundRawMessage


class ConnectUpdateOutboundEmailContent(BaseModel):
    MessageSourceType: Literal['RAW']
    RawMessage: ConnectUpdateOutboundRawMessage
