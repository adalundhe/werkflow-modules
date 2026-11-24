from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubGetApplicationRequest(BaseModel):
    ApplicationIdentifier: StrictStr
    EnvironmentIdentifier: StrictStr
