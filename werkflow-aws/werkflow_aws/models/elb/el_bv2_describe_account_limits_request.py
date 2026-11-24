from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ELBv2DescribeAccountLimitsRequest(BaseModel):
    Marker: StrictStr | None = None
    PageSize: StrictInt | None = None
