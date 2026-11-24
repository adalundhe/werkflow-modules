from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetOperationsRequest(BaseModel):
    pageToken: StrictStr | None = None
