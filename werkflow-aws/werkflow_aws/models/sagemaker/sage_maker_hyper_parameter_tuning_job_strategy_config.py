from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_hyperband_strategy_config import SageMakerHyperbandStrategyConfig


class SageMakerHyperParameterTuningJobStrategyConfig(BaseModel):
    HyperbandStrategyConfig: SageMakerHyperbandStrategyConfig | None = None
