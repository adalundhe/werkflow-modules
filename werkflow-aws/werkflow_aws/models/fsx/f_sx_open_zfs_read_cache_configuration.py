from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FSxOpenZFSReadCacheConfiguration(BaseModel):
    SizingMode: StrictStr | None = None
    SizeGiB: StrictInt | None = None
