from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteCustomerGatewayRequest(BaseModel):
    CustomerGatewayId: StrictStr
    DryRun: StrictBool | None = None
