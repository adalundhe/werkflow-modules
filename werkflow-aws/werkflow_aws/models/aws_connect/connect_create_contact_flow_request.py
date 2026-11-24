from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectCreateContactFlowRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
    Type: Literal['CONTACT_FLOW', 'CUSTOMER_QUEUE', 'CUSTOMER_HOLD', 'CUSTOMER_WHISPER', 'AGENT_HOLD', 'AGENT_WHISPER', 'OUTBOUND_WHISPER', 'AGENT_TRANSFER', 'QUEUE_TRANSFER', 'CAMPAIGN']
    Content: StrictStr
    Description: StrictStr | None = None
    Status: Literal['PUBLISHED', 'SAVED'] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
