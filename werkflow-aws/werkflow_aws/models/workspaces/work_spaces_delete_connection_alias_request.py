from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesDeleteConnectionAliasRequest(BaseModel):
    AliasId: StrictStr
