from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessDocumentAttributeConfiguration(BaseModel):
    name: StrictStr | None = None
    type: StrictStr | None = None
    search: StrictStr | None = None
