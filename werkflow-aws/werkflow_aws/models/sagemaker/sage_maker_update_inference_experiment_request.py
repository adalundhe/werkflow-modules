from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_inference_experiment_data_storage_config import SageMakerInferenceExperimentDataStorageConfig
from .sage_maker_inference_experiment_schedule import SageMakerInferenceExperimentSchedule
from .sage_maker_model_variant_config import SageMakerModelVariantConfig
from .sage_maker_shadow_mode_config import SageMakerShadowModeConfig


class SageMakerUpdateInferenceExperimentRequest(BaseModel):
    Name: StrictStr
    Schedule: SageMakerInferenceExperimentSchedule | None = None
    Description: StrictStr | None = None
    ModelVariants: list[SageMakerModelVariantConfig] | None = None
    DataStorageConfig: SageMakerInferenceExperimentDataStorageConfig | None = None
    ShadowModeConfig: SageMakerShadowModeConfig | None = None
