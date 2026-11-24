from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAdditionalNotes(BaseModel):
    Text: StrictStr | None = None
