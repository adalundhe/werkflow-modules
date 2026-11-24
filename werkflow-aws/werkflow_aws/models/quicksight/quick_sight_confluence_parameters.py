from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightConfluenceParameters(BaseModel):
    ConfluenceUrl: StrictStr | None = None
