from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerDeregistrationPolicy(BaseModel):
    deleteResources: StrictStr | None = None
