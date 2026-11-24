from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSBatchAssociateResourceRequest(BaseModel):
    ResourceSetIdentifier: StrictStr
    Items: list[StrictStr]
