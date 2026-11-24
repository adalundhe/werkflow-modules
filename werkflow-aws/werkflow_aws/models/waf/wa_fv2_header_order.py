from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2HeaderOrder(BaseModel):
    OversizeHandling: StrictStr | None = None
