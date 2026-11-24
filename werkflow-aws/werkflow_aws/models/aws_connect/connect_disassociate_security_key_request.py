from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDisassociateSecurityKeyRequest(BaseModel):
    InstanceId: StrictStr
    AssociationId: StrictStr
    ClientToken: StrictStr | None = None
