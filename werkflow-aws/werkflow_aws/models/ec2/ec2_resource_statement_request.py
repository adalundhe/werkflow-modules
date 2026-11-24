from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ResourceStatementRequest(BaseModel):
    Resources: list[StrictStr] | None = None
    ResourceTypes: list[StrictStr] | None = None
