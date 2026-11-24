from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceResourceKey(BaseModel):
    resourceType: StrictStr | None = None
    resourceId: StrictStr | None = None
