from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaSelfManagedEventSourceModel(BaseModel):
    Endpoints: dict[StrictStr, list[StrictStr]] | None = None
