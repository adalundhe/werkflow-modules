from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectDisassociateFlowRequest(BaseModel):
    InstanceId: StrictStr
    ResourceId: StrictStr
    ResourceType: Literal['SMS_PHONE_NUMBER', 'INBOUND_EMAIL', 'OUTBOUND_EMAIL', 'ANALYTICS_CONNECTOR', 'WHATSAPP_MESSAGING_PHONE_NUMBER']
