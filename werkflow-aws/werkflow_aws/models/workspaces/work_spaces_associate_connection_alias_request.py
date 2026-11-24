from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesAssociateConnectionAliasRequest(BaseModel):
    AliasId: StrictStr
    ResourceId: StrictStr
