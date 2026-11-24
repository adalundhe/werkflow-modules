from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2PutPortalProductSharingPolicyRequest(BaseModel):
    PolicyDocument: StrictStr
    PortalProductId: StrictStr
