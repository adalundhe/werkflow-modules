from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListContactFlowsRequest(BaseModel):
    InstanceId: StrictStr
    ContactFlowTypes: list[Literal['CONTACT_FLOW', 'CUSTOMER_QUEUE', 'CUSTOMER_HOLD', 'CUSTOMER_WHISPER', 'AGENT_HOLD', 'AGENT_WHISPER', 'OUTBOUND_WHISPER', 'AGENT_TRANSFER', 'QUEUE_TRANSFER', 'CAMPAIGN']] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
