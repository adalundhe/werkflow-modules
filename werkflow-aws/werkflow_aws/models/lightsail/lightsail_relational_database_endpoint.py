from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LightsailRelationalDatabaseEndpoint(BaseModel):
    port: StrictInt | None = None
    address: StrictStr | None = None
