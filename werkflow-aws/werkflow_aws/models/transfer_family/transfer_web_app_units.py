from __future__ import annotations
from pydantic import BaseModel, StrictInt


class TransferWebAppUnits(BaseModel):
    Provisioned: StrictInt | None = None
