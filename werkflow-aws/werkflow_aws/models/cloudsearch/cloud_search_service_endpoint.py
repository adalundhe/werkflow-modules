from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudSearchServiceEndpoint(BaseModel):
    Endpoint: StrictStr | None = None
