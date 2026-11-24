from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectBatchGetFlowAssociationRequest(BaseModel):
    InstanceId: StrictStr
    ResourceIds: list[StrictStr]
    ResourceType: Literal['WHATSAPP_MESSAGING_PHONE_NUMBER', 'VOICE_PHONE_NUMBER', 'INBOUND_EMAIL', 'OUTBOUND_EMAIL', 'ANALYTICS_CONNECTOR'] | None = None
