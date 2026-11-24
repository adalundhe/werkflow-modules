from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LocationLteLocalId(BaseModel):
    Earfcn: StrictInt
    Pci: StrictInt
