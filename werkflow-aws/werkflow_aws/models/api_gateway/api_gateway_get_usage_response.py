from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class APIGatewayGetUsageResponse(BaseModel):
    usagePlanId: StrictStr | None = None
    startDate: StrictStr | None = None
    endDate: StrictStr | None = None
    position: StrictStr | None = None
    items: dict[StrictStr, list[list[StrictInt]]] | None = None
    ResponseMetadata: dict[str, Any] | None = None
