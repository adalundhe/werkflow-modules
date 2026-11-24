from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubUrlEndpointConfig(BaseModel):
    HealthUrl: StrictStr | None = None
    Url: StrictStr | None = None
