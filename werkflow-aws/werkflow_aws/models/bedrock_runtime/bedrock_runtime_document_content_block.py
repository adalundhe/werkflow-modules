from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeDocumentContentBlock(BaseModel):
    text: StrictStr | None = None
