from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ManagedGrafanaServiceAccountTokenSummary(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    expiresAt: datetime.datetime | StrictStr | None = None
    lastUsedAt: datetime.datetime | StrictStr | None = None
