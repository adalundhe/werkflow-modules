from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUserQuickConnectConfig(BaseModel):
    UserId: StrictStr | None = None
    ContactFlowId: StrictStr | None = None
