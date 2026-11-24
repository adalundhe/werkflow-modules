from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceResourceFilters(BaseModel):
    AccountId: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceName: StrictStr | None = None
    Region: StrictStr | None = None
