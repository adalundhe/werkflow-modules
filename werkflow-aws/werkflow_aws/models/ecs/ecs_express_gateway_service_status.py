from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSExpressGatewayServiceStatus(BaseModel):
    statusCode: StrictStr | None = None
    statusReason: StrictStr | None = None
