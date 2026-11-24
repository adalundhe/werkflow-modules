from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_generation_configuration import BedrockGenerationConfiguration
from .bedrock_knowledge_base_retrieval_configuration import BedrockKnowledgeBaseRetrievalConfiguration
from .bedrock_orchestration_configuration import BedrockOrchestrationConfiguration


class BedrockKnowledgeBaseRetrieveAndGenerateConfiguration(BaseModel):
    knowledgeBaseId: StrictStr | None = None
    modelArn: StrictStr | None = None
    retrievalConfiguration: BedrockKnowledgeBaseRetrievalConfiguration | None = None
    generationConfiguration: BedrockGenerationConfiguration | None = None
    orchestrationConfiguration: BedrockOrchestrationConfiguration | None = None
