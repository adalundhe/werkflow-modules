from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerRecommendationJobPayloadConfig(BaseModel):
    SamplePayloadUrl: StrictStr | None = None
    SupportedContentTypes: list[StrictStr] | None = None
