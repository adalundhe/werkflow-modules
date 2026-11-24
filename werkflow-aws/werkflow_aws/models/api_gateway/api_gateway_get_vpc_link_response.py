from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class APIGatewayGetVpcLinkResponse(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    targetArns: list[StrictStr] | None = None
    status: StrictStr | None = None
    statusMessage: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
