from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ECSGatewayConnectorDeregistrationDelay(BaseModel):
    timeoutSeconds: StrictInt | None = None
