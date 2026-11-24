from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ComprehendChildBlock(BaseModel):
    ChildBlockId: StrictStr | None = None
    BeginOffset: StrictInt | None = None
    EndOffset: StrictInt | None = None
