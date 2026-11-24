from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedGrafanaServiceAccountTokenSummaryWithKey(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    key: StrictStr | None = None
