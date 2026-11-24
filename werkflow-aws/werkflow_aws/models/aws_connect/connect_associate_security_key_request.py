from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAssociateSecurityKeyRequest(BaseModel):
    InstanceId: StrictStr
    Key: StrictStr
    ClientToken: StrictStr | None = None
