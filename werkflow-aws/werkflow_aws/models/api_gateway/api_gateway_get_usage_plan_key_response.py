from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class APIGatewayGetUsagePlanKeyResponse(BaseModel):
    id: StrictStr | None = None
    type: StrictStr | None = None
    value: StrictStr | None = None
    name: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
