from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraFailedEntity(BaseModel):
    EntityId: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
