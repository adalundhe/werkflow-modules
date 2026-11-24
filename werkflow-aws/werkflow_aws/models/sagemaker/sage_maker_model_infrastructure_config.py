from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_real_time_inference_config import SageMakerRealTimeInferenceConfig


class SageMakerModelInfrastructureConfig(BaseModel):
    InfrastructureType: StrictStr | None = None
    RealTimeInferenceConfig: SageMakerRealTimeInferenceConfig | None = None
