from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxDeleteSnapmirrorPolicyRequest(BaseModel):
    SnapmirrorPolicyId: StrictStr
    ClientRequestToken: StrictStr | None = None
