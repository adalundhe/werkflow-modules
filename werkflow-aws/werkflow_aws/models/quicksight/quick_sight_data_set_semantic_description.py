from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDataSetSemanticDescription(BaseModel):
    Text: StrictStr | None = None
