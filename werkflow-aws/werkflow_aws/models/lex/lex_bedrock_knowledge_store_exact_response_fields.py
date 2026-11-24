from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexBedrockKnowledgeStoreExactResponseFields(BaseModel):
    answerField: StrictStr | None = None
