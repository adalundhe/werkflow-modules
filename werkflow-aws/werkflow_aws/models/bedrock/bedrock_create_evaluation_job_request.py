from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .bedrock_evaluation_config import BedrockEvaluationConfig
from .bedrock_evaluation_inference_config import BedrockEvaluationInferenceConfig
from .bedrock_evaluation_output_data_config import BedrockEvaluationOutputDataConfig
from .bedrock_tag import BedrockTag


class BedrockCreateEvaluationJobRequest(BaseModel):
    jobName: StrictStr
    roleArn: StrictStr
    evaluationConfig: BedrockEvaluationConfig
    inferenceConfig: BedrockEvaluationInferenceConfig
    outputDataConfig: BedrockEvaluationOutputDataConfig
    jobDescription: StrictStr | None = None
    clientRequestToken: StrictStr | None = None
    customerEncryptionKeyId: StrictStr | None = None
    jobTags: list[BedrockTag] | None = None
    applicationType: Literal['ModelEvaluation', 'RagEvaluation'] | None = None
