from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MacieGroupCount(BaseModel):
    count: StrictInt | None = None
    groupKey: StrictStr | None = None
