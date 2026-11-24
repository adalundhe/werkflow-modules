from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MigrationHubListServicesRequest(BaseModel):
    ApplicationIdentifier: StrictStr
    EnvironmentIdentifier: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
