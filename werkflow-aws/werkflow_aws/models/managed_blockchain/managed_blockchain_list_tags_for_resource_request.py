from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedBlockchainListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
