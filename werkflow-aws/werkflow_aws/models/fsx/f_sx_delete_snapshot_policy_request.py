from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxDeleteSnapshotPolicyRequest(BaseModel):
    SnapshotPolicyId: StrictStr
    ClientRequestToken: StrictStr | None = None
