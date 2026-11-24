from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SESPutAccountDedicatedIpWarmupAttributesRequest(BaseModel):
    AutoWarmupEnabled: StrictBool | None = None
