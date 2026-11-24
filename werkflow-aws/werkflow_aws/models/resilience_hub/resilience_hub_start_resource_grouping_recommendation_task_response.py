from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ResilienceHubStartResourceGroupingRecommendationTaskResponse(BaseModel):
    appArn: StrictStr | None = None
    errorMessage: StrictStr | None = None
    groupingId: StrictStr | None = None
    status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
