from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruServiceCollection(BaseModel):
    ServiceNames: list[StrictStr] | None = None
