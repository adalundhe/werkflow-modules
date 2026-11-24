from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectChatEntryPointParameters(BaseModel):
    FlowId: StrictStr | None = None
