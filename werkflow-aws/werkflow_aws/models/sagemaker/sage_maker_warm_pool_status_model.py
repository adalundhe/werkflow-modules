from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerWarmPoolStatusModel(BaseModel):
    Status: StrictStr | None = None
    ResourceRetainedBillableTimeInSeconds: StrictInt | None = None
    ReusedByJob: StrictStr | None = None
