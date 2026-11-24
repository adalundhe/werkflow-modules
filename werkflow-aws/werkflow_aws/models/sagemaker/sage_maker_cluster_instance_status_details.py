from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerClusterInstanceStatusDetails(BaseModel):
    Status: StrictStr | None = None
    Message: StrictStr | None = None
