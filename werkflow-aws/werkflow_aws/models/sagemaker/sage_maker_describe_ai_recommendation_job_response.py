from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_ai_adapter_source import SageMakerAIAdapterSource
from .sage_maker_ai_model_source import SageMakerAIModelSource
from .sage_maker_ai_recommendation import SageMakerAIRecommendation
from .sage_maker_ai_recommendation_compute_spec import SageMakerAIRecommendationComputeSpec
from .sage_maker_ai_recommendation_inference_specification import SageMakerAIRecommendationInferenceSpecification
from .sage_maker_ai_recommendation_output_result import SageMakerAIRecommendationOutputResult
from .sage_maker_ai_recommendation_performance_target import SageMakerAIRecommendationPerformanceTarget
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerDescribeAIRecommendationJobResponse(BaseModel):
    AIRecommendationJobName: StrictStr | None = None
    AIRecommendationJobArn: StrictStr | None = None
    AIRecommendationJobStatus: StrictStr | None = None
    FailureReason: StrictStr | None = None
    ModelSource: SageMakerAIModelSource | None = None
    OutputConfig: SageMakerAIRecommendationOutputResult | None = None
    InferenceSpecification: SageMakerAIRecommendationInferenceSpecification | None = None
    AIWorkloadConfigIdentifier: StrictStr | None = None
    OptimizeModel: StrictBool | None = None
    PerformanceTarget: SageMakerAIRecommendationPerformanceTarget | None = None
    Recommendations: list[SageMakerAIRecommendation] | None = None
    RoleArn: StrictStr | None = None
    ComputeSpec: SageMakerAIRecommendationComputeSpec | None = None
    AdapterSource: SageMakerAIAdapterSource | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
