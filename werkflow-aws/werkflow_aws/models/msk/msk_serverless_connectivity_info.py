from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKServerlessConnectivityInfo(BaseModel):
    NetworkType: StrictStr | None = None
