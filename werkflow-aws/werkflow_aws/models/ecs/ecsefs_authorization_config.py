from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSEFSAuthorizationConfig(BaseModel):
    accessPointId: StrictStr | None = None
    iam: StrictStr | None = None
