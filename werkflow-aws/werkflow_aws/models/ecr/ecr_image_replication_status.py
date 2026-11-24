from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRImageReplicationStatus(BaseModel):
    region: StrictStr | None = None
    registryId: StrictStr | None = None
    status: StrictStr | None = None
    failureCode: StrictStr | None = None
