from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightTableFieldCustomIconContent(BaseModel):
    Icon: StrictStr | None = None
