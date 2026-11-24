from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBDeleteDBSubnetGroupRequest(BaseModel):
    DBSubnetGroupName: StrictStr
