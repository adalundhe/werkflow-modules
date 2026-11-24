from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightReferenceLineCustomLabelConfiguration(BaseModel):
    CustomLabel: StrictStr | None = None
