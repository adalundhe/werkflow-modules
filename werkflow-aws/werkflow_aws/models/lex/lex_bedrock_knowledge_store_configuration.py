from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .lex_bedrock_knowledge_store_exact_response_fields import LexBedrockKnowledgeStoreExactResponseFields


class LexBedrockKnowledgeStoreConfiguration(BaseModel):
    bedrockKnowledgeBaseArn: StrictStr | None = None
    exactResponse: StrictBool | None = None
    exactResponseFields: LexBedrockKnowledgeStoreExactResponseFields | None = None
