from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MediaStoreGetMetricPolicyRequest(BaseModel):
    ContainerName: StrictStr
