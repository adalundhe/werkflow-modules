from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectFlowQuickConnectConfig(BaseModel):
    ContactFlowId: StrictStr | None = None
