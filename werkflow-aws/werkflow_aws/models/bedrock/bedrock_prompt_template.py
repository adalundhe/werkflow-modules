from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockPromptTemplate(BaseModel):
    textPromptTemplate: StrictStr | None = None
