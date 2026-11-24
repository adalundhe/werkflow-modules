from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_outbound_email_config import ConnectOutboundEmailConfig


class ConnectUpdateQueueOutboundEmailConfigRequest(BaseModel):
    InstanceId: StrictStr
    QueueId: StrictStr
    OutboundEmailConfig: ConnectOutboundEmailConfig
