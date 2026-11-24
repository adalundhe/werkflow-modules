from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightNegativeFormat(BaseModel):
    Prefix: StrictStr | None = None
    Suffix: StrictStr | None = None
