from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComputeOptimizerIdleRecommendationError(BaseModel):
    identifier: StrictStr | None = None
    code: StrictStr | None = None
    message: StrictStr | None = None
    resourceType: StrictStr | None = None
