from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_container_definition_model import SageMakerContainerDefinitionModel
from .sage_maker_deployment_recommendation_model import SageMakerDeploymentRecommendationModel
from .sage_maker_inference_execution_config_model import SageMakerInferenceExecutionConfigModel
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_vpc_config_model import SageMakerVpcConfigModel


class SageMakerModel(BaseModel):
    ModelName: StrictStr | None = None
    PrimaryContainer: SageMakerContainerDefinitionModel | None = None
    Containers: list[SageMakerContainerDefinitionModel] | None = None
    InferenceExecutionConfig: SageMakerInferenceExecutionConfigModel | None = None
    ExecutionRoleArn: StrictStr | None = None
    VpcConfig: SageMakerVpcConfigModel | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ModelArn: StrictStr | None = None
    EnableNetworkIsolation: StrictBool | None = None
    Tags: list[SageMakerTagModel] | None = None
    DeploymentRecommendation: SageMakerDeploymentRecommendationModel | None = None
