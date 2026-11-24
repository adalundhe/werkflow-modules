from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceConfigSnapshotDeliveryProperties(BaseModel):
    deliveryFrequency: StrictStr | None = None
