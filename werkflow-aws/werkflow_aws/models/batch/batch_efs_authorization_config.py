from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchEFSAuthorizationConfig(BaseModel):
    accessPointId: StrictStr | None = None
    iam: StrictStr | None = None
