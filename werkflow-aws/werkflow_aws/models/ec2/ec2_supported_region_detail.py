from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2SupportedRegionDetail(BaseModel):
    Region: StrictStr | None = None
    ServiceState: StrictStr | None = None
