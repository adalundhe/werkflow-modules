from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectStopBgpFailoverTestRequest(BaseModel):
    virtualInterfaceId: StrictStr
