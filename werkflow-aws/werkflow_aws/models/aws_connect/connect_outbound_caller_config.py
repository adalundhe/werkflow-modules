from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectOutboundCallerConfig(BaseModel):
    OutboundCallerIdName: StrictStr | None = None
    OutboundCallerIdNumberId: StrictStr | None = None
    OutboundFlowId: StrictStr | None = None
