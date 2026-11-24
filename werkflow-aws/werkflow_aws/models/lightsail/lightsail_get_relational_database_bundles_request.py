from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailGetRelationalDatabaseBundlesRequest(BaseModel):
    pageToken: StrictStr | None = None
    includeInactive: StrictBool | None = None
