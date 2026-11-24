from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ConnectAutoAcceptConfig(BaseModel):
    Channel: StrictStr | None = None
    AutoAccept: StrictBool | None = None
    AgentFirstCallbackAutoAccept: StrictBool | None = None
