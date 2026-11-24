from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListFlowAssociationsRequest(BaseModel):
    InstanceId: StrictStr
    ResourceType: Literal['WHATSAPP_MESSAGING_PHONE_NUMBER', 'VOICE_PHONE_NUMBER', 'INBOUND_EMAIL', 'OUTBOUND_EMAIL', 'ANALYTICS_CONNECTOR'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
