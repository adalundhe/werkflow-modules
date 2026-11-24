from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowTrendmicroSourceProperties(BaseModel):
    object: StrictStr | None = None
