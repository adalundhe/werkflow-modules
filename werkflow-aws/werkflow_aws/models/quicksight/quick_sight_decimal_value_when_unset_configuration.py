from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class QuickSightDecimalValueWhenUnsetConfiguration(BaseModel):
    ValueWhenUnsetOption: StrictStr | None = None
    CustomValue: StrictFloat | StrictInt | None = None
