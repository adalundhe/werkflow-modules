from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMStartAssociationsOnceRequest(BaseModel):
    AssociationIds: list[StrictStr]
