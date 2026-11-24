from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class BatchShareAttributes(BaseModel):
    shareIdentifier: StrictStr | None = None
    weightFactor: StrictFloat | StrictInt | None = None
