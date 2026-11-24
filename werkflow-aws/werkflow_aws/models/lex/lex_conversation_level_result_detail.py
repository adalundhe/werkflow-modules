from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexConversationLevelResultDetail(BaseModel):
    endToEndResult: StrictStr | None = None
    speechTranscriptionResult: StrictStr | None = None
