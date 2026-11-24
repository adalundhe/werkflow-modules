from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerClusterInstanceTypeDetail(BaseModel):
    InstanceType: StrictStr | None = None
    CurrentCount: StrictInt | None = None
    ThreadsPerCore: StrictInt | None = None
