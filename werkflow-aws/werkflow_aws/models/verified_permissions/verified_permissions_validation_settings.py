from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsValidationSettings(BaseModel):
    mode: StrictStr | None = None
