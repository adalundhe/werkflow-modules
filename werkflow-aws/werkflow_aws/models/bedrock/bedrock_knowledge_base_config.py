from __future__ import annotations
from pydantic import BaseModel
from .bedrock_retrieve_and_generate_configuration import BedrockRetrieveAndGenerateConfiguration
from .bedrock_retrieve_config import BedrockRetrieveConfig


class BedrockKnowledgeBaseConfig(BaseModel):
    retrieveConfig: BedrockRetrieveConfig | None = None
    retrieveAndGenerateConfig: BedrockRetrieveAndGenerateConfiguration | None = None
