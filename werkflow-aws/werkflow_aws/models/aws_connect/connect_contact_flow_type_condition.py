from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ConnectContactFlowTypeCondition(BaseModel):
    ContactFlowType: Literal['CONTACT_FLOW', 'CUSTOMER_QUEUE', 'CUSTOMER_HOLD', 'CUSTOMER_WHISPER', 'AGENT_HOLD', 'AGENT_WHISPER', 'OUTBOUND_WHISPER', 'AGENT_TRANSFER', 'QUEUE_TRANSFER', 'CAMPAIGN'] | None = None
