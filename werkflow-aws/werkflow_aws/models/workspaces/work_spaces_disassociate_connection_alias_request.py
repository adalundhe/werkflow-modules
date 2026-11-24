from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesDisassociateConnectionAliasRequest(BaseModel):
    AliasId: StrictStr
