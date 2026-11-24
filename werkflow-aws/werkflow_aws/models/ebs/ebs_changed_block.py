from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EBSChangedBlock(BaseModel):
    BlockIndex: StrictInt | None = None
    FirstBlockToken: StrictStr | None = None
    SecondBlockToken: StrictStr | None = None
