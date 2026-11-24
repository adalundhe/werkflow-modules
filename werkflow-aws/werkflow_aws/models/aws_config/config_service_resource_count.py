from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConfigServiceResourceCount(BaseModel):
    resourceType: StrictStr | None = None
    count: StrictInt | None = None
