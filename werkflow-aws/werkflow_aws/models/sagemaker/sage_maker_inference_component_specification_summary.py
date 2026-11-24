from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_inference_component_compute_resource_requirements import SageMakerInferenceComponentComputeResourceRequirements
from .sage_maker_inference_component_container_specification_summary import SageMakerInferenceComponentContainerSpecificationSummary
from .sage_maker_inference_component_data_cache_config_summary import SageMakerInferenceComponentDataCacheConfigSummary
from .sage_maker_inference_component_scheduling_config import SageMakerInferenceComponentSchedulingConfig
from .sage_maker_inference_component_startup_parameters import SageMakerInferenceComponentStartupParameters


class SageMakerInferenceComponentSpecificationSummary(BaseModel):
    InstanceType: StrictStr | None = None
    ModelName: StrictStr | None = None
    Container: SageMakerInferenceComponentContainerSpecificationSummary | None = None
    StartupParameters: SageMakerInferenceComponentStartupParameters | None = None
    ComputeResourceRequirements: SageMakerInferenceComponentComputeResourceRequirements | None = None
    BaseInferenceComponentName: StrictStr | None = None
    DataCacheConfig: SageMakerInferenceComponentDataCacheConfigSummary | None = None
    SchedulingConfig: SageMakerInferenceComponentSchedulingConfig | None = None
