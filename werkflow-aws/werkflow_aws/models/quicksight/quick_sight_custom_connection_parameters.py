from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightCustomConnectionParameters(BaseModel):
    ConnectionType: StrictStr | None = None
