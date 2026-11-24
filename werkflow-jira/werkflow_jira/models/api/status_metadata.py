from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StatusMetadata(BaseModel):
    category: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
