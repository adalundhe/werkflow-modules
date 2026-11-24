from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedGrafanaServiceAccountSummary(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    isDisabled: StrictStr | None = None
    grafanaRole: StrictStr | None = None
