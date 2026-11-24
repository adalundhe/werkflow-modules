from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConfigServiceGroupedResourceCount(BaseModel):
    GroupName: StrictStr | None = None
    ResourceCount: StrictInt | None = None
