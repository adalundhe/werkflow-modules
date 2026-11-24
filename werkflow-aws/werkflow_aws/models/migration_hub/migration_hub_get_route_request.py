from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubGetRouteRequest(BaseModel):
    ApplicationIdentifier: StrictStr
    EnvironmentIdentifier: StrictStr
    RouteIdentifier: StrictStr
