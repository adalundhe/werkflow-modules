from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .connect_string_condition import ConnectStringCondition


class ConnectContactFlowSearchCriteria(BaseModel):
    OrConditions: list[ConnectContactFlowSearchCriteria] | None = None
    AndConditions: list[ConnectContactFlowSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
    TypeCondition: Literal['CONTACT_FLOW', 'CUSTOMER_QUEUE', 'CUSTOMER_HOLD', 'CUSTOMER_WHISPER', 'AGENT_HOLD', 'AGENT_WHISPER', 'OUTBOUND_WHISPER', 'AGENT_TRANSFER', 'QUEUE_TRANSFER', 'CAMPAIGN'] | None = None
    StateCondition: Literal['ACTIVE', 'ARCHIVED'] | None = None
    StatusCondition: Literal['PUBLISHED', 'SAVED'] | None = None
