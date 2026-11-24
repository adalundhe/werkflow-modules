from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightReferenceLineStyleConfiguration(BaseModel):
    Pattern: StrictStr | None = None
    Color: StrictStr | None = None
