from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisGetResourcePolicyRequest(BaseModel):
    ResourceARN: StrictStr
    StreamId: StrictStr | None = None
