from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexConversationLevelSlotResolutionResultItem(BaseModel):
    intentName: StrictStr | None = None
    slotName: StrictStr | None = None
    matchResult: StrictStr | None = None
