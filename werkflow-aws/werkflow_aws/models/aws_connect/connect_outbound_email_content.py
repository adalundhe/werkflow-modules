from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .connect_outbound_raw_message import ConnectOutboundRawMessage
from .connect_templated_message_config import ConnectTemplatedMessageConfig


class ConnectOutboundEmailContent(BaseModel):
    MessageSourceType: Literal['TEMPLATE', 'RAW']
    TemplatedMessageConfig: ConnectTemplatedMessageConfig | None = None
    RawMessage: ConnectOutboundRawMessage | None = None
