from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveRelatedFindingDetail(BaseModel):
    Arn: StrictStr | None = None
    Type: StrictStr | None = None
    IpAddress: StrictStr | None = None
