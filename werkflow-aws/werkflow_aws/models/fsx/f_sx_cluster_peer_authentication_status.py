from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxClusterPeerAuthenticationStatus(BaseModel):
    State: StrictStr | None = None
    InUse: StrictStr | None = None
