from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_custom_model_data_source import BedrockCustomModelDataSource
from .bedrock_model_data_source import BedrockModelDataSource
from .bedrock_tag import BedrockTag


class BedrockCreateCustomModelRequest(BaseModel):
    modelName: StrictStr
    modelSourceConfig: BedrockModelDataSource | None = None
    customModelDataSource: BedrockCustomModelDataSource | None = None
    modelKmsKeyArn: StrictStr | None = None
    roleArn: StrictStr | None = None
    modelTags: list[BedrockTag] | None = None
    clientRequestToken: StrictStr | None = None
