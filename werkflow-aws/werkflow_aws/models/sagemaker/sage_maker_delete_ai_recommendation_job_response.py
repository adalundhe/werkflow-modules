from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerDeleteAIRecommendationJobResponse(BaseModel):
    AIRecommendationJobArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
