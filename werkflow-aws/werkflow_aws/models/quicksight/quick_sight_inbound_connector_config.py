from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightInboundConnectorConfig(BaseModel):
    InboundConnectorType: StrictStr | None = None
