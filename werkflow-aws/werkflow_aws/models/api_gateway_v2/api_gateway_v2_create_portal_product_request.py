from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2CreatePortalProductRequest(BaseModel):
    DisplayName: StrictStr
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
