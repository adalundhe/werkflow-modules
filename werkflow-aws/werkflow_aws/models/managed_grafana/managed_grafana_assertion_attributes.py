from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedGrafanaAssertionAttributes(BaseModel):
    name: StrictStr | None = None
    login: StrictStr | None = None
    email: StrictStr | None = None
    groups: StrictStr | None = None
    role: StrictStr | None = None
    org: StrictStr | None = None
