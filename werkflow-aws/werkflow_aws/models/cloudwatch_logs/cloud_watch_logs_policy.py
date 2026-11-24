from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsPolicy(BaseModel):
    deliveryDestinationPolicy: StrictStr | None = None
