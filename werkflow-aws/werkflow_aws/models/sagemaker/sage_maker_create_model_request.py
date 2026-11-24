from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_container_definition import SageMakerContainerDefinition
from .sage_maker_inference_execution_config import SageMakerInferenceExecutionConfig
from .sage_maker_tag import SageMakerTag
from .sage_maker_vpc_config import SageMakerVpcConfig


class SageMakerCreateModelRequest(BaseModel):
    ModelName: StrictStr
    PrimaryContainer: SageMakerContainerDefinition | None = None
    Containers: list[SageMakerContainerDefinition] | None = None
    InferenceExecutionConfig: SageMakerInferenceExecutionConfig | None = None
    ExecutionRoleArn: StrictStr | None = None
    Tags: list[SageMakerTag] | None = None
    VpcConfig: SageMakerVpcConfig | None = None
    EnableNetworkIsolation: StrictBool | None = None
