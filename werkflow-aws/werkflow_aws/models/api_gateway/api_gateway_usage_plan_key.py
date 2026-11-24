from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayUsagePlanKey(BaseModel):
    id: StrictStr | None = None
    type: StrictStr | None = None
    value: StrictStr | None = None
    name: StrictStr | None = None
