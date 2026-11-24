from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
