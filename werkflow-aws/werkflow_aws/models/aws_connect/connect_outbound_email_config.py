from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectOutboundEmailConfig(BaseModel):
    OutboundEmailAddressId: StrictStr | None = None
