from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class MacieServiceLimit(BaseModel):
    isServiceLimited: StrictBool | None = None
    unit: StrictStr | None = None
    value: StrictInt | None = None
