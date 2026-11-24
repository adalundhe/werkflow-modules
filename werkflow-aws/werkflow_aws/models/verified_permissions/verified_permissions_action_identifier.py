from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsActionIdentifier(BaseModel):
    actionType: StrictStr | None = None
    actionId: StrictStr | None = None
