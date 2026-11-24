from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_bias import SageMakerBias
from .sage_maker_explainability import SageMakerExplainability
from .sage_maker_model_data_quality import SageMakerModelDataQuality
from .sage_maker_model_quality import SageMakerModelQuality


class SageMakerModelMetrics(BaseModel):
    ModelQuality: SageMakerModelQuality | None = None
    ModelDataQuality: SageMakerModelDataQuality | None = None
    Bias: SageMakerBias | None = None
    Explainability: SageMakerExplainability | None = None
