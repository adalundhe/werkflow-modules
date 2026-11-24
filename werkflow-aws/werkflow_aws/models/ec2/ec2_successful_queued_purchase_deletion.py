from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2SuccessfulQueuedPurchaseDeletion(BaseModel):
    ReservedInstancesId: StrictStr | None = None
