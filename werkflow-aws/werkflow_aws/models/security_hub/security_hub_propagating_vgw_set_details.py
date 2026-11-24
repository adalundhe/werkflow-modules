from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubPropagatingVgwSetDetails(BaseModel):
    GatewayId: StrictStr | None = None
