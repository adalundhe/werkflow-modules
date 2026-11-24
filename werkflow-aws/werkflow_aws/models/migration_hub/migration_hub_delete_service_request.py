from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubDeleteServiceRequest(BaseModel):
    ApplicationIdentifier: StrictStr
    EnvironmentIdentifier: StrictStr
    ServiceIdentifier: StrictStr
