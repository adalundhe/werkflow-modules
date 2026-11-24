from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_outbound_caller_config import ConnectOutboundCallerConfig


class ConnectUpdateQueueOutboundCallerConfigRequest(BaseModel):
    InstanceId: StrictStr
    QueueId: StrictStr
    OutboundCallerConfig: ConnectOutboundCallerConfig
