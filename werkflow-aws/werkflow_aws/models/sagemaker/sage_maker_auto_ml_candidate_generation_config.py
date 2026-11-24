from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_auto_ml_algorithm_config import SageMakerAutoMLAlgorithmConfig


class SageMakerAutoMLCandidateGenerationConfig(BaseModel):
    FeatureSpecificationS3Uri: StrictStr | None = None
    AlgorithmsConfig: list[SageMakerAutoMLAlgorithmConfig] | None = None
