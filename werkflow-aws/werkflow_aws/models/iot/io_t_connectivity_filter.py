from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTConnectivityFilter(BaseModel):
    includeSocketInformation: list[StrictStr] | None = None
