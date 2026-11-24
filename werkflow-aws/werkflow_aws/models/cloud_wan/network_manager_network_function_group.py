from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerNetworkFunctionGroup(BaseModel):
    Name: StrictStr | None = None
