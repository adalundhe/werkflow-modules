from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_endpoint_info import SageMakerEndpointInfo
from .sage_maker_endpoint_input_configuration import SageMakerEndpointInputConfiguration
from .sage_maker_recommendation_job_container_config import SageMakerRecommendationJobContainerConfig
from .sage_maker_recommendation_job_resource_limit import SageMakerRecommendationJobResourceLimit
from .sage_maker_recommendation_job_vpc_config import SageMakerRecommendationJobVpcConfig
from .sage_maker_traffic_pattern import SageMakerTrafficPattern


class SageMakerRecommendationJobInputConfig(BaseModel):
    ModelPackageVersionArn: StrictStr | None = None
    ModelName: StrictStr | None = None
    JobDurationInSeconds: StrictInt | None = None
    TrafficPattern: SageMakerTrafficPattern | None = None
    ResourceLimit: SageMakerRecommendationJobResourceLimit | None = None
    EndpointConfigurations: list[SageMakerEndpointInputConfiguration] | None = None
    VolumeKmsKeyId: StrictStr | None = None
    ContainerConfig: SageMakerRecommendationJobContainerConfig | None = None
    Endpoints: list[SageMakerEndpointInfo] | None = None
    VpcConfig: SageMakerRecommendationJobVpcConfig | None = None
