from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2FlexCostAllocationOperationFailure(BaseModel):
    ResourceId: StrictStr | None = None
    FailureCode: StrictStr | None = None
    FailureReason: StrictStr | None = None
