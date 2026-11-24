from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexConversationLevelIntentClassificationResultItem(BaseModel):
    intentName: StrictStr | None = None
    matchResult: StrictStr | None = None
