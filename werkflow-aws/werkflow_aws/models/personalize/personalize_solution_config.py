from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .personalize_auto_ml_config import PersonalizeAutoMLConfig
from .personalize_auto_training_config import PersonalizeAutoTrainingConfig
from .personalize_events_config import PersonalizeEventsConfig
from .personalize_hpo_config import PersonalizeHPOConfig
from .personalize_optimization_objective import PersonalizeOptimizationObjective
from .personalize_training_data_config import PersonalizeTrainingDataConfig


class PersonalizeSolutionConfig(BaseModel):
    eventValueThreshold: StrictStr | None = None
    hpoConfig: PersonalizeHPOConfig | None = None
    algorithmHyperParameters: dict[StrictStr, StrictStr] | None = None
    featureTransformationParameters: dict[StrictStr, StrictStr] | None = None
    autoMLConfig: PersonalizeAutoMLConfig | None = None
    eventsConfig: PersonalizeEventsConfig | None = None
    optimizationObjective: PersonalizeOptimizationObjective | None = None
    trainingDataConfig: PersonalizeTrainingDataConfig | None = None
    autoTrainingConfig: PersonalizeAutoTrainingConfig | None = None
