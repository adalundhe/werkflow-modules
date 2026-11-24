from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRReplicationDestination(BaseModel):
    region: StrictStr | None = None
    registryId: StrictStr | None = None
