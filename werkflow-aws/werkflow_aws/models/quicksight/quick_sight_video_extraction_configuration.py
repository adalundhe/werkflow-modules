from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightVideoExtractionConfiguration(BaseModel):
    videoExtractionStatus: StrictStr | None = None
    videoExtractionType: StrictStr | None = None
