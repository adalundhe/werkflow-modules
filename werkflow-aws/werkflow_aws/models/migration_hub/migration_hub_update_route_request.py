from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class MigrationHubUpdateRouteRequest(BaseModel):
    ActivationState: Literal['ACTIVE', 'INACTIVE']
    ApplicationIdentifier: StrictStr
    EnvironmentIdentifier: StrictStr
    RouteIdentifier: StrictStr
