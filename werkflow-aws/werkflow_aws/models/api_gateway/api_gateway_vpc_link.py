from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayVpcLink(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    targetArns: list[StrictStr] | None = None
    status: StrictStr | None = None
    statusMessage: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
