from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerDefaultExportDestination(BaseModel):
    destinationType: StrictStr | None = None
    destination: StrictStr | None = None
