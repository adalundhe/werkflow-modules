from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_evaluation_config import BedrockEvaluationConfig
from .bedrock_evaluation_inference_config import BedrockEvaluationInferenceConfig
from .bedrock_evaluation_output_data_config import BedrockEvaluationOutputDataConfig


class BedrockGetEvaluationJobResponse(BaseModel):
    jobName: StrictStr | None = None
    status: StrictStr | None = None
    jobArn: StrictStr | None = None
    jobDescription: StrictStr | None = None
    roleArn: StrictStr | None = None
    customerEncryptionKeyId: StrictStr | None = None
    jobType: StrictStr | None = None
    applicationType: StrictStr | None = None
    evaluationConfig: BedrockEvaluationConfig | None = None
    inferenceConfig: BedrockEvaluationInferenceConfig | None = None
    outputDataConfig: BedrockEvaluationOutputDataConfig | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    lastModifiedTime: datetime.datetime | StrictStr | None = None
    failureMessages: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
