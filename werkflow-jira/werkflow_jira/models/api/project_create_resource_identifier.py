from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ProjectCreateResourceIdentifier(BaseModel):
    anID: StrictBool | None = None
    areference: StrictBool | None = None
    entityId: StrictStr | None = None
    entityType: StrictStr | None = None
    id: StrictStr | None = None
    type: StrictStr | None = None
