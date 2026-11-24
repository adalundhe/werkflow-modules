from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerServiceMetadata(BaseModel):
    name: StrictStr | None = None
    displayName: StrictStr | None = None
    description: StrictStr | None = None
    category: StrictStr | None = None
