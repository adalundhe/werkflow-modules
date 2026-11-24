from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisPutResourcePolicyRequest(BaseModel):
    ResourceARN: StrictStr
    Policy: StrictStr
    StreamId: StrictStr | None = None
