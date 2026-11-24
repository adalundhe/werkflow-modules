from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ECSGatewaySummary(BaseModel):
    gatewayArn: StrictStr | None = None
    name: StrictStr | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
