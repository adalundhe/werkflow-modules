from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .sage_maker_clarify_shap_baseline_config import SageMakerClarifyShapBaselineConfig
from .sage_maker_clarify_text_config import SageMakerClarifyTextConfig


class SageMakerClarifyShapConfig(BaseModel):
    ShapBaselineConfig: SageMakerClarifyShapBaselineConfig | None = None
    NumberOfSamples: StrictInt | None = None
    UseLogit: StrictBool | None = None
    Seed: StrictInt | None = None
    TextConfig: SageMakerClarifyTextConfig | None = None
