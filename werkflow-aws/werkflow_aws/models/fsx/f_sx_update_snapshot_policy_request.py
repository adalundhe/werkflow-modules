from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FSxUpdateSnapshotPolicyRequest(BaseModel):
    SnapshotPolicyId: StrictStr
    ClientRequestToken: StrictStr | None = None
    Enabled: StrictBool | None = None
