from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchSchedulingPolicyListingDetail(BaseModel):
    arn: StrictStr | None = None
