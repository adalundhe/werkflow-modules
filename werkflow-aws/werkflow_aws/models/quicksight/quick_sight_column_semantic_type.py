from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightColumnSemanticType(BaseModel):
    GeographicalRole: StrictStr | None = None
