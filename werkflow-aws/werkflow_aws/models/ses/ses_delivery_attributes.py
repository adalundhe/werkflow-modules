from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESDeliveryAttributes(BaseModel):
    SharedPoolDeliveryMode: StrictStr | None = None
