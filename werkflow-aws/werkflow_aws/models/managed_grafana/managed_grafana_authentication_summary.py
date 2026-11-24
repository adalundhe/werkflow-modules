from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedGrafanaAuthenticationSummary(BaseModel):
    providers: list[StrictStr] | None = None
    samlConfigurationStatus: StrictStr | None = None
