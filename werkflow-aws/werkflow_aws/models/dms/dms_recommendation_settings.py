from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSRecommendationSettings(BaseModel):
    InstanceSizingType: StrictStr | None = None
    WorkloadType: StrictStr | None = None
