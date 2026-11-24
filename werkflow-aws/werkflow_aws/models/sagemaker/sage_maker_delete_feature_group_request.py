from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteFeatureGroupRequest(BaseModel):
    FeatureGroupName: StrictStr
