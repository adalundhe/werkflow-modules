from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmListOfferingTransactionsRequest(BaseModel):
    nextToken: StrictStr | None = None
