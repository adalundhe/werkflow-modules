from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_ai_recommendation_adapter_details import SageMakerAIRecommendationAdapterDetails
from .sage_maker_ai_recommendation_deployment_configuration import SageMakerAIRecommendationDeploymentConfiguration
from .sage_maker_ai_recommendation_model_details import SageMakerAIRecommendationModelDetails
from .sage_maker_ai_recommendation_optimization_detail import SageMakerAIRecommendationOptimizationDetail
from .sage_maker_ai_recommendation_performance_metric import SageMakerAIRecommendationPerformanceMetric


class SageMakerAIRecommendation(BaseModel):
    RecommendationDescription: StrictStr | None = None
    OptimizationDetails: list[SageMakerAIRecommendationOptimizationDetail] | None = None
    ModelDetails: SageMakerAIRecommendationModelDetails | None = None
    DeploymentConfiguration: SageMakerAIRecommendationDeploymentConfiguration | None = None
    AIBenchmarkJobArn: StrictStr | None = None
    ExpectedPerformance: list[SageMakerAIRecommendationPerformanceMetric] | None = None
    AdapterDetails: SageMakerAIRecommendationAdapterDetails | None = None
