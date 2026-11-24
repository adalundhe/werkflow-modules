from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKRebalancing(BaseModel):
    Status: StrictStr | None = None
