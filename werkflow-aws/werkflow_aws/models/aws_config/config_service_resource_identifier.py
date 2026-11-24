from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConfigServiceResourceIdentifier(BaseModel):
    resourceType: StrictStr | None = None
    resourceId: StrictStr | None = None
    resourceName: StrictStr | None = None
    resourceDeletionTime: datetime.datetime | StrictStr | None = None
