from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_clarify_inference_config import SageMakerClarifyInferenceConfig
from .sage_maker_clarify_shap_config import SageMakerClarifyShapConfig


class SageMakerClarifyExplainerConfig(BaseModel):
    EnableExplanations: StrictStr | None = None
    InferenceConfig: SageMakerClarifyInferenceConfig | None = None
    ShapConfig: SageMakerClarifyShapConfig | None = None
