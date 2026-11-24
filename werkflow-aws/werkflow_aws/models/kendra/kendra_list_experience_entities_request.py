from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraListExperienceEntitiesRequest(BaseModel):
    Id: StrictStr
    IndexId: StrictStr
    NextToken: StrictStr | None = None
