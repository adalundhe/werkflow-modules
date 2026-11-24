from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAssociateApprovedOriginRequest(BaseModel):
    InstanceId: StrictStr
    Origin: StrictStr
    ClientToken: StrictStr | None = None
