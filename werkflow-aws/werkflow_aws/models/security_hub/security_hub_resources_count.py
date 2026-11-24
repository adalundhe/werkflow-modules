from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubResourcesCount(BaseModel):
    AllResources: StrictInt | None = None
