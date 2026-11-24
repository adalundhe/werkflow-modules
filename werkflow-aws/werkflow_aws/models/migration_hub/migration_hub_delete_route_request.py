from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubDeleteRouteRequest(BaseModel):
    ApplicationIdentifier: StrictStr
    EnvironmentIdentifier: StrictStr
    RouteIdentifier: StrictStr
