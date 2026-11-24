from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteInstanceRequest(BaseModel):
    InstanceId: StrictStr
    ClientToken: StrictStr | None = None
