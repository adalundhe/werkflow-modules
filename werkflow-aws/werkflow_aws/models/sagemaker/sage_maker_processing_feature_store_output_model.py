from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerProcessingFeatureStoreOutputModel(BaseModel):
    FeatureGroupName: StrictStr | None = None
