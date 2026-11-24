from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceRelationship(BaseModel):
    resourceType: StrictStr | None = None
    resourceId: StrictStr | None = None
    resourceName: StrictStr | None = None
    relationshipName: StrictStr | None = None
