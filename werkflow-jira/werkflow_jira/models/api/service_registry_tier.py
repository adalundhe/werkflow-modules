from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceRegistryTier(BaseModel):
    description: StrictStr | None = None
    id: StrictStr | None = None
    level: StrictInt | None = None
    name: StrictStr | None = None
    nameKey: StrictStr | None = None
