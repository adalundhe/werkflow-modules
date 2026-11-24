from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDeleteExpressGatewayServiceRequest(BaseModel):
    serviceArn: StrictStr
