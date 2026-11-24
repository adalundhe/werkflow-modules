from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueBetweenConfiguration(BaseModel):
    LowBoundKey: StrictStr | None = None
    HighBoundKey: StrictStr | None = None
    Template: StrictStr | None = None
