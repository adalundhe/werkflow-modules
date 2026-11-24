from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSUpdateGatewayNetworkConfiguration(BaseModel):
    inboundSecurityGroup: StrictStr | None = None
