from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MigrationHubListEnvironmentsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
