from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerPriorityClass(BaseModel):
    Name: StrictStr | None = None
    Weight: StrictInt | None = None
