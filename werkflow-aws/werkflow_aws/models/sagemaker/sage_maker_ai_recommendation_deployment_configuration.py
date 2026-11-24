from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_ai_recommendation_deployment_s3_channel import SageMakerAIRecommendationDeploymentS3Channel


class SageMakerAIRecommendationDeploymentConfiguration(BaseModel):
    S3: list[SageMakerAIRecommendationDeploymentS3Channel] | None = None
    ImageUri: StrictStr | None = None
    InstanceType: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    CopyCountPerInstance: StrictInt | None = None
    EnvironmentVariables: dict[StrictStr, StrictStr] | None = None
    MinCpuMemoryRequiredInMb: StrictInt | None = None
