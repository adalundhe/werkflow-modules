from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayCreateVpcLinkRequest(BaseModel):
    name: StrictStr
    targetArns: list[StrictStr]
    description: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
