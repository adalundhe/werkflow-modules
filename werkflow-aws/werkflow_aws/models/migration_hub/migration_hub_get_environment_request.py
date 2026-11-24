from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubGetEnvironmentRequest(BaseModel):
    EnvironmentIdentifier: StrictStr
