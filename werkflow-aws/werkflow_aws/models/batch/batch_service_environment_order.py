from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BatchServiceEnvironmentOrder(BaseModel):
    order: StrictInt | None = None
    serviceEnvironment: StrictStr | None = None
