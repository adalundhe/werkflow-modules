from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .bedrock_model_invocation_job_input_data_config import BedrockModelInvocationJobInputDataConfig
from .bedrock_model_invocation_job_output_data_config import BedrockModelInvocationJobOutputDataConfig
from .bedrock_tag import BedrockTag
from .bedrock_vpc_config import BedrockVpcConfig


class BedrockCreateModelInvocationJobRequest(BaseModel):
    jobName: StrictStr
    roleArn: StrictStr
    modelId: StrictStr
    inputDataConfig: BedrockModelInvocationJobInputDataConfig
    outputDataConfig: BedrockModelInvocationJobOutputDataConfig
    clientRequestToken: StrictStr | None = None
    vpcConfig: BedrockVpcConfig | None = None
    timeoutDurationInHours: StrictInt | None = None
    tags: list[BedrockTag] | None = None
    modelInvocationType: Literal['InvokeModel', 'Converse'] | None = None
