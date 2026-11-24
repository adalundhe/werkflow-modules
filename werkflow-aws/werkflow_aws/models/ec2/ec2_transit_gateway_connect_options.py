from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TransitGatewayConnectOptions(BaseModel):
    Protocol: StrictStr | None = None
