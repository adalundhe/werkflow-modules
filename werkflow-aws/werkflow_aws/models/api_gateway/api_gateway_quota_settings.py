from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class APIGatewayQuotaSettings(BaseModel):
    limit: StrictInt | None = None
    offset: StrictInt | None = None
    period: StrictStr | None = None
