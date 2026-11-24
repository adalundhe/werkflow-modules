from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class EntityPropertyDetails(BaseModel):
    entityId: StrictFloat | StrictInt | None = None
    key: StrictStr | None = None
    value: StrictStr | None = None
