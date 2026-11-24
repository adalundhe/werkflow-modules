from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FSxDiskIopsConfiguration(BaseModel):
    Mode: StrictStr | None = None
    Iops: StrictInt | None = None
