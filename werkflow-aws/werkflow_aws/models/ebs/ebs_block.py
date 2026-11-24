from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EBSBlock(BaseModel):
    BlockIndex: StrictInt | None = None
    BlockToken: StrictStr | None = None
