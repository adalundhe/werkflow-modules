from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDataPathLabelType(BaseModel):
    FieldId: StrictStr | None = None
    FieldValue: StrictStr | None = None
    Visibility: StrictStr | None = None
