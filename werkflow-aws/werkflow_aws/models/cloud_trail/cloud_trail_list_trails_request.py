from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailListTrailsRequest(BaseModel):
    NextToken: StrictStr | None = None
