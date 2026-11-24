from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LicensedApplication(BaseModel):
    id: StrictStr | None = None
    plan: StrictStr | None = None
