from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsApplicationOperationDescription(BaseModel):
    ApplicationOperationId: StrictStr | None = None
    ApplicationName: StrictStr | None = None
