from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectDeleteLagRequest(BaseModel):
    lagId: StrictStr
