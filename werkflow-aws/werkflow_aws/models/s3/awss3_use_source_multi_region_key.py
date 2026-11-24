from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3UseSourceMultiRegionKey(BaseModel):
    Status: StrictStr | None = None
