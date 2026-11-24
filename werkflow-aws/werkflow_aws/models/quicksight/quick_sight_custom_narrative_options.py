from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightCustomNarrativeOptions(BaseModel):
    Narrative: StrictStr | None = None
