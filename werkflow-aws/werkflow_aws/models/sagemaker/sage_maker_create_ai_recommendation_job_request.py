from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_ai_adapter_source import SageMakerAIAdapterSource
from .sage_maker_ai_model_source import SageMakerAIModelSource
from .sage_maker_ai_recommendation_compute_spec import SageMakerAIRecommendationComputeSpec
from .sage_maker_ai_recommendation_inference_specification import SageMakerAIRecommendationInferenceSpecification
from .sage_maker_ai_recommendation_output_config import SageMakerAIRecommendationOutputConfig
from .sage_maker_ai_recommendation_performance_target import SageMakerAIRecommendationPerformanceTarget
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateAIRecommendationJobRequest(BaseModel):
    AIRecommendationJobName: StrictStr
    ModelSource: SageMakerAIModelSource
    OutputConfig: SageMakerAIRecommendationOutputConfig
    AIWorkloadConfigIdentifier: StrictStr
    PerformanceTarget: SageMakerAIRecommendationPerformanceTarget
    RoleArn: StrictStr
    InferenceSpecification: SageMakerAIRecommendationInferenceSpecification | None = None
    OptimizeModel: StrictBool | None = None
    ComputeSpec: SageMakerAIRecommendationComputeSpec | None = None
    AdapterSource: SageMakerAIAdapterSource | None = None
    Tags: list[SageMakerTagModel] | None = None
