from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
