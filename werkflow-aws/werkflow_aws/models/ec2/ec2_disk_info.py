from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2DiskInfo(BaseModel):
    SizeInGB: StrictInt | None = None
    Count: StrictInt | None = None
    Type: StrictStr | None = None
