from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2Body(BaseModel):
    OversizeHandling: StrictStr | None = None
