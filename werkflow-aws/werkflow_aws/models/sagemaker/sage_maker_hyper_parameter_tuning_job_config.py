from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_hyper_parameter_tuning_job_objective import SageMakerHyperParameterTuningJobObjective
from .sage_maker_hyper_parameter_tuning_job_strategy_config import SageMakerHyperParameterTuningJobStrategyConfig
from .sage_maker_parameter_ranges import SageMakerParameterRanges
from .sage_maker_resource_limits import SageMakerResourceLimits
from .sage_maker_tuning_job_completion_criteria import SageMakerTuningJobCompletionCriteria


class SageMakerHyperParameterTuningJobConfig(BaseModel):
    Strategy: StrictStr | None = None
    StrategyConfig: SageMakerHyperParameterTuningJobStrategyConfig | None = None
    HyperParameterTuningJobObjective: SageMakerHyperParameterTuningJobObjective | None = None
    ResourceLimits: SageMakerResourceLimits | None = None
    ParameterRanges: SageMakerParameterRanges | None = None
    TrainingJobEarlyStoppingType: StrictStr | None = None
    TuningJobCompletionCriteria: SageMakerTuningJobCompletionCriteria | None = None
    RandomSeed: StrictInt | None = None
