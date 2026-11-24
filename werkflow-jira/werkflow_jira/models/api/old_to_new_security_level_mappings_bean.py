from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OldToNewSecurityLevelMappingsBean(BaseModel):
    newLevelId: StrictStr | None = None
    oldLevelId: StrictStr | None = None
