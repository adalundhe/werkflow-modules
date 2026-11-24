from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MediaStoreMetricPolicyRule(BaseModel):
    ObjectGroup: StrictStr | None = None
    ObjectGroupName: StrictStr | None = None
