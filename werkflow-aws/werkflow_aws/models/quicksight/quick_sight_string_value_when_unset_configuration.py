from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightStringValueWhenUnsetConfiguration(BaseModel):
    ValueWhenUnsetOption: StrictStr | None = None
    CustomValue: StrictStr | None = None
