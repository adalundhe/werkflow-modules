from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MigrationHubListApplicationsRequest(BaseModel):
    EnvironmentIdentifier: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
