from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightIdentifier(BaseModel):
    Identity: StrictStr | None = None
