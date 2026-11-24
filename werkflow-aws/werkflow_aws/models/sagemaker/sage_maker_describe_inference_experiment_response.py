from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_endpoint_metadata import SageMakerEndpointMetadata
from .sage_maker_inference_experiment_data_storage_config import SageMakerInferenceExperimentDataStorageConfig
from .sage_maker_inference_experiment_schedule import SageMakerInferenceExperimentSchedule
from .sage_maker_model_variant_config_summary import SageMakerModelVariantConfigSummary
from .sage_maker_shadow_mode_config import SageMakerShadowModeConfig


class SageMakerDescribeInferenceExperimentResponse(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Schedule: SageMakerInferenceExperimentSchedule | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    Description: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CompletionTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    RoleArn: StrictStr | None = None
    EndpointMetadata: SageMakerEndpointMetadata | None = None
    ModelVariants: list[SageMakerModelVariantConfigSummary] | None = None
    DataStorageConfig: SageMakerInferenceExperimentDataStorageConfig | None = None
    ShadowModeConfig: SageMakerShadowModeConfig | None = None
    KmsKey: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
