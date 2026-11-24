from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSGatewayConnectorHealthCheckMatcher(BaseModel):
    httpCode: StrictStr | None = None
    grpcCode: StrictStr | None = None
