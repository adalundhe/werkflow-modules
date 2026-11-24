from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_model_data_source import BedrockModelDataSource
from .bedrock_tag import BedrockTag
from .bedrock_vpc_config import BedrockVpcConfig


class BedrockCreateModelImportJobRequest(BaseModel):
    jobName: StrictStr
    importedModelName: StrictStr
    roleArn: StrictStr
    modelDataSource: BedrockModelDataSource
    jobTags: list[BedrockTag] | None = None
    importedModelTags: list[BedrockTag] | None = None
    clientRequestToken: StrictStr | None = None
    vpcConfig: BedrockVpcConfig | None = None
    importedModelKmsKeyId: StrictStr | None = None
