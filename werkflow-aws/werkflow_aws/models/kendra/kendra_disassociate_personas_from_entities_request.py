from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDisassociatePersonasFromEntitiesRequest(BaseModel):
    Id: StrictStr
    IndexId: StrictStr
    EntityIds: list[StrictStr]
