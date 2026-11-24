from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetPortalProductSharingPolicyResponse(BaseModel):
    PolicyDocument: StrictStr | None = None
    PortalProductId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
