from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightNamedEntitySort(BaseModel):
    FieldName: StrictStr | None = None
    Direction: StrictStr | None = None
