from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .bedrock_model_invocation_job_input_data_config import BedrockModelInvocationJobInputDataConfig
from .bedrock_model_invocation_job_output_data_config import BedrockModelInvocationJobOutputDataConfig
from .bedrock_vpc_config import BedrockVpcConfig


class BedrockModelInvocationJobSummary(BaseModel):
    jobArn: StrictStr | None = None
    jobName: StrictStr | None = None
    modelId: StrictStr | None = None
    clientRequestToken: StrictStr | None = None
    roleArn: StrictStr | None = None
    status: StrictStr | None = None
    message: StrictStr | None = None
    submitTime: datetime.datetime | StrictStr | None = None
    lastModifiedTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    inputDataConfig: BedrockModelInvocationJobInputDataConfig | None = None
    outputDataConfig: BedrockModelInvocationJobOutputDataConfig | None = None
    vpcConfig: BedrockVpcConfig | None = None
    timeoutDurationInHours: StrictInt | None = None
    jobExpirationTime: datetime.datetime | StrictStr | None = None
    modelInvocationType: StrictStr | None = None
    totalRecordCount: StrictInt | None = None
    processedRecordCount: StrictInt | None = None
    successRecordCount: StrictInt | None = None
    errorRecordCount: StrictInt | None = None
