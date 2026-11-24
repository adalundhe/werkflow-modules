from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_async_inference_config import SageMakerAsyncInferenceConfig
from .sage_maker_cross_region_traffic_config import SageMakerCrossRegionTrafficConfig
from .sage_maker_data_capture_config_summary import SageMakerDataCaptureConfigSummary
from .sage_maker_deployment_config import SageMakerDeploymentConfig
from .sage_maker_endpoint_status import SageMakerEndpointStatus
from .sage_maker_explainer_config import SageMakerExplainerConfig
from .sage_maker_metrics_config import SageMakerMetricsConfig
from .sage_maker_pending_deployment_summary import SageMakerPendingDeploymentSummary
from .sage_maker_production_variant_summary import SageMakerProductionVariantSummary


class SageMakerDescribeEndpointResponse(BaseModel):
    EndpointName: StrictStr | None = None
    EndpointArn: StrictStr | None = None
    EndpointConfigName: StrictStr | None = None
    ProductionVariants: list[SageMakerProductionVariantSummary] | None = None
    DataCaptureConfig: SageMakerDataCaptureConfigSummary | None = None
    EndpointStatus: SageMakerEndpointStatus | None = None
    FailureReason: StrictStr | None = None
    CreationTime: datetime.datetime | None = None
    LastModifiedTime: datetime.datetime | None = None
    LastDeploymentConfig: SageMakerDeploymentConfig | None = None
    AsyncInferenceConfig: SageMakerAsyncInferenceConfig | None = None
    PendingDeploymentSummary: SageMakerPendingDeploymentSummary | None = None
    ExplainerConfig: SageMakerExplainerConfig | None = None
    ShadowProductionVariants: list[SageMakerProductionVariantSummary] | None = None
    MetricsConfig: SageMakerMetricsConfig | None = None
    CrossRegionTrafficConfig: SageMakerCrossRegionTrafficConfig | None = None
