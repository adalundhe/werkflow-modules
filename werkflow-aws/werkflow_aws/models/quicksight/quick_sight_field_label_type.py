from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightFieldLabelType(BaseModel):
    FieldId: StrictStr | None = None
    Visibility: StrictStr | None = None
