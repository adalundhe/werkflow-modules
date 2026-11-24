from __future__ import annotations
from pydantic import BaseModel
from .lex_bedrock_knowledge_store_configuration import LexBedrockKnowledgeStoreConfiguration
from .lex_opensearch_configuration import LexOpensearchConfiguration
from .lex_qn_a_kendra_configuration import LexQnAKendraConfiguration


class LexDataSourceConfiguration(BaseModel):
    opensearchConfiguration: LexOpensearchConfiguration | None = None
    kendraConfiguration: LexQnAKendraConfiguration | None = None
    bedrockKnowledgeStoreConfiguration: LexBedrockKnowledgeStoreConfiguration | None = None
