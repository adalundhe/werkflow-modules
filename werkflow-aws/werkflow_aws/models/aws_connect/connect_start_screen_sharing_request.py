from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectStartScreenSharingRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    ClientToken: StrictStr | None = None
