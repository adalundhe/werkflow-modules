from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockFieldForReranking(BaseModel):
    fieldName: StrictStr | None = None
