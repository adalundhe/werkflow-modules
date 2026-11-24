from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightIntegerValueWhenUnsetConfiguration(BaseModel):
    ValueWhenUnsetOption: StrictStr | None = None
    CustomValue: StrictInt | None = None
