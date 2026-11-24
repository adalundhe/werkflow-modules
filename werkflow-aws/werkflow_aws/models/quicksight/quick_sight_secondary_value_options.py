from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSecondaryValueOptions(BaseModel):
    Visibility: StrictStr | None = None
