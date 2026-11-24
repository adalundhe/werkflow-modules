from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_async_inference_config import SageMakerAsyncInferenceConfig
from .sage_maker_cross_region_traffic_config import SageMakerCrossRegionTrafficConfig
from .sage_maker_data_capture_config import SageMakerDataCaptureConfig
from .sage_maker_explainer_config import SageMakerExplainerConfig
from .sage_maker_metrics_config import SageMakerMetricsConfig
from .sage_maker_production_variant import SageMakerProductionVariant
from .sage_maker_tag import SageMakerTag
from .sage_maker_vpc_config import SageMakerVpcConfig


class SageMakerCreateEndpointConfigRequest(BaseModel):
    EndpointConfigName: StrictStr
    ProductionVariants: list[SageMakerProductionVariant]
    DataCaptureConfig: SageMakerDataCaptureConfig | None = None
    Tags: list[SageMakerTag] | None = None
    KmsKeyId: StrictStr | None = None
    AsyncInferenceConfig: SageMakerAsyncInferenceConfig | None = None
    ExplainerConfig: SageMakerExplainerConfig | None = None
    ShadowProductionVariants: list[SageMakerProductionVariant] | None = None
    ExecutionRoleArn: StrictStr | None = None
    VpcConfig: SageMakerVpcConfig | None = None
    EnableNetworkIsolation: StrictBool | None = None
    MetricsConfig: SageMakerMetricsConfig | None = None
    CrossRegionTrafficConfig: SageMakerCrossRegionTrafficConfig | None = None
