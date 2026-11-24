from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MediaStoreDeleteMetricPolicyRequest(BaseModel):
    ContainerName: StrictStr
