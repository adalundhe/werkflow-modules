from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_container_definition import SageMakerContainerDefinition
from .sage_maker_deployment_recommendation import SageMakerDeploymentRecommendation
from .sage_maker_inference_execution_config import SageMakerInferenceExecutionConfig
from .sage_maker_vpc_config import SageMakerVpcConfig


class SageMakerDescribeModelResponse(BaseModel):
    ModelName: StrictStr | None = None
    PrimaryContainer: SageMakerContainerDefinition | None = None
    Containers: list[SageMakerContainerDefinition] | None = None
    InferenceExecutionConfig: SageMakerInferenceExecutionConfig | None = None
    ExecutionRoleArn: StrictStr | None = None
    VpcConfig: SageMakerVpcConfig | None = None
    CreationTime: datetime.datetime | None = None
    ModelArn: StrictStr | None = None
    EnableNetworkIsolation: StrictBool | None = None
    DeploymentRecommendation: SageMakerDeploymentRecommendation | None = None
