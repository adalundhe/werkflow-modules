from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: dict[StrictStr, StrictStr]
