from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeKinesisParameters(BaseModel):
    PartitionKeyPath: StrictStr | None = None
