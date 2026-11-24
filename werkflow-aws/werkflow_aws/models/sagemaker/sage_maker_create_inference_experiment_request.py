from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .sage_maker_inference_experiment_data_storage_config import SageMakerInferenceExperimentDataStorageConfig
from .sage_maker_inference_experiment_schedule import SageMakerInferenceExperimentSchedule
from .sage_maker_model_variant_config import SageMakerModelVariantConfig
from .sage_maker_shadow_mode_config import SageMakerShadowModeConfig
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateInferenceExperimentRequest(BaseModel):
    Name: StrictStr
    Type: Literal['ShadowMode']
    RoleArn: StrictStr
    EndpointName: StrictStr
    ModelVariants: list[SageMakerModelVariantConfig]
    ShadowModeConfig: SageMakerShadowModeConfig
    Schedule: SageMakerInferenceExperimentSchedule | None = None
    Description: StrictStr | None = None
    DataStorageConfig: SageMakerInferenceExperimentDataStorageConfig | None = None
    KmsKey: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
