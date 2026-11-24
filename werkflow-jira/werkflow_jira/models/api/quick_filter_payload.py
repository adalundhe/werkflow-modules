from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickFilterPayload(BaseModel):
    description: StrictStr | None = None
    jqlQuery: StrictStr | None = None
    name: StrictStr | None = None
