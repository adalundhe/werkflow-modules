from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubUrlEndpointInput(BaseModel):
    HealthUrl: StrictStr | None = None
    Url: StrictStr | None = None
