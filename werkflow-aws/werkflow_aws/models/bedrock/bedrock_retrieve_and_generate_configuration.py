from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_external_sources_retrieve_and_generate_configuration import BedrockExternalSourcesRetrieveAndGenerateConfiguration
from .bedrock_knowledge_base_retrieve_and_generate_configuration import BedrockKnowledgeBaseRetrieveAndGenerateConfiguration


class BedrockRetrieveAndGenerateConfiguration(BaseModel):
    type: StrictStr | None = None
    knowledgeBaseConfiguration: BedrockKnowledgeBaseRetrieveAndGenerateConfiguration | None = None
    externalSourcesConfiguration: BedrockExternalSourcesRetrieveAndGenerateConfiguration | None = None
