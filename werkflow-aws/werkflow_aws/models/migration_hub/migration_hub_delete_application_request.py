from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubDeleteApplicationRequest(BaseModel):
    ApplicationIdentifier: StrictStr
    EnvironmentIdentifier: StrictStr
