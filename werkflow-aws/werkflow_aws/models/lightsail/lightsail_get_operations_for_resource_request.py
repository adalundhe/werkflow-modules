from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetOperationsForResourceRequest(BaseModel):
    resourceName: StrictStr
    pageToken: StrictStr | None = None
