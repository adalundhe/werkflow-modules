from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class RekognitionCustomizationFeatureContentModerationConfig(BaseModel):
    ConfidenceThreshold: StrictFloat | StrictInt | None = None
