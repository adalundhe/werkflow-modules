from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateParticipantAuthenticationRequest(BaseModel):
    State: StrictStr
    InstanceId: StrictStr
    Code: StrictStr | None = None
    Error: StrictStr | None = None
    ErrorDescription: StrictStr | None = None
