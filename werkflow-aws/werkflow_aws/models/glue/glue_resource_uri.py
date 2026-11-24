from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GlueResourceUri(BaseModel):
    ResourceType: StrictStr | None = None
    Uri: StrictStr | None = None
    LastModified: datetime.datetime | StrictStr | None = None
