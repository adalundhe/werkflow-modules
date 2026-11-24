from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3InventoryFilter(BaseModel):
    Prefix: StrictStr | None = None
