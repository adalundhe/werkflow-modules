from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectPauseContactRequest(BaseModel):
    ContactId: StrictStr
    InstanceId: StrictStr
    ContactFlowId: StrictStr | None = None
