from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerProcessingFeatureStoreOutput(BaseModel):
    FeatureGroupName: StrictStr | None = None
