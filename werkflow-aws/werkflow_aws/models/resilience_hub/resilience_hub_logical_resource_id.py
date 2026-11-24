from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubLogicalResourceId(BaseModel):
    eksSourceName: StrictStr | None = None
    identifier: StrictStr | None = None
    logicalStackName: StrictStr | None = None
    resourceGroupName: StrictStr | None = None
    terraformSourceName: StrictStr | None = None
