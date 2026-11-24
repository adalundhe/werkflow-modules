from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisDeleteResourcePolicyRequest(BaseModel):
    ResourceARN: StrictStr
    StreamId: StrictStr | None = None
