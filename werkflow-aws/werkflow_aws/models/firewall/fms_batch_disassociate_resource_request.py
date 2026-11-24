from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSBatchDisassociateResourceRequest(BaseModel):
    ResourceSetIdentifier: StrictStr
    Items: list[StrictStr]
