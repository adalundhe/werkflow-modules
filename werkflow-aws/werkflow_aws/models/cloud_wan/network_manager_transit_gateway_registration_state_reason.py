from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerTransitGatewayRegistrationStateReason(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
