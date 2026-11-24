from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAIRecommendationDeploymentS3Channel(BaseModel):
    ChannelName: StrictStr | None = None
    Uri: StrictStr | None = None
