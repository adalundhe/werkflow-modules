from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessPluginTypeMetadataSummary(BaseModel):
    type: StrictStr | None = None
    category: StrictStr | None = None
    description: StrictStr | None = None
