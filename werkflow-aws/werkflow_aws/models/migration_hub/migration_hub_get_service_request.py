from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubGetServiceRequest(BaseModel):
    ApplicationIdentifier: StrictStr
    EnvironmentIdentifier: StrictStr
    ServiceIdentifier: StrictStr
