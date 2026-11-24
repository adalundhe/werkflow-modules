from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_auto_ml_algorithm_config import SageMakerAutoMLAlgorithmConfig


class SageMakerCandidateGenerationConfig(BaseModel):
    AlgorithmsConfig: list[SageMakerAutoMLAlgorithmConfig] | None = None
