from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightCustomActionURLOperation(BaseModel):
    URLTemplate: StrictStr | None = None
    URLTarget: StrictStr | None = None
