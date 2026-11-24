from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSMultiRegionKey(BaseModel):
    Arn: StrictStr | None = None
    Region: StrictStr | None = None
