from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerShadowModelVariantConfig(BaseModel):
    ShadowModelVariantName: StrictStr | None = None
    SamplingPercentage: StrictInt | None = None
