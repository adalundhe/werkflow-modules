from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerRecommendationJobCompiledOutputConfig(BaseModel):
    S3OutputUri: StrictStr | None = None
