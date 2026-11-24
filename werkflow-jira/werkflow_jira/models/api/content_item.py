from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ContentItem(BaseModel):
    entityId: StrictStr | None = None
    entityType: StrictStr | None = None
    id: StrictStr | None = None
