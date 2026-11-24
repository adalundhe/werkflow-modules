from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_drift_check_bias import SageMakerDriftCheckBias
from .sage_maker_drift_check_explainability import SageMakerDriftCheckExplainability
from .sage_maker_drift_check_model_data_quality import SageMakerDriftCheckModelDataQuality
from .sage_maker_drift_check_model_quality import SageMakerDriftCheckModelQuality


class SageMakerDriftCheckBaselines(BaseModel):
    Bias: SageMakerDriftCheckBias | None = None
    Explainability: SageMakerDriftCheckExplainability | None = None
    ModelQuality: SageMakerDriftCheckModelQuality | None = None
    ModelDataQuality: SageMakerDriftCheckModelDataQuality | None = None
