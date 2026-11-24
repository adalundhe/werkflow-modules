from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_endpoint_output_configuration import SageMakerEndpointOutputConfiguration
from .sage_maker_inference_metrics import SageMakerInferenceMetrics
from .sage_maker_model_configuration import SageMakerModelConfiguration
from .sage_maker_recommendation_metrics import SageMakerRecommendationMetrics


class SageMakerRecommendationJobInferenceBenchmark(BaseModel):
    Metrics: SageMakerRecommendationMetrics | None = None
    EndpointMetrics: SageMakerInferenceMetrics | None = None
    EndpointConfiguration: SageMakerEndpointOutputConfiguration | None = None
    ModelConfiguration: SageMakerModelConfiguration | None = None
    FailureReason: StrictStr | None = None
    InvocationEndTime: datetime.datetime | StrictStr | None = None
    InvocationStartTime: datetime.datetime | StrictStr | None = None
