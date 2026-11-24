from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MacieRecord(BaseModel):
    jsonPath: StrictStr | None = None
    recordIndex: StrictInt | None = None
