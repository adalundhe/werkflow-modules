from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceResourceCountFilters(BaseModel):
    ResourceType: StrictStr | None = None
    AccountId: StrictStr | None = None
    Region: StrictStr | None = None
