from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class LocationLteNetworkMeasurements(BaseModel):
    Earfcn: StrictInt
    CellId: StrictInt
    Pci: StrictInt
    Rsrp: StrictInt | None = None
    Rsrq: StrictFloat | StrictInt | None = None
