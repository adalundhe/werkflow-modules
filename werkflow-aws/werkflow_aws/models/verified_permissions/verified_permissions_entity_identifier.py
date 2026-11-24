from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsEntityIdentifier(BaseModel):
    entityType: StrictStr | None = None
    entityId: StrictStr | None = None
