from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedBlockchainUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
