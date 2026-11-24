from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class LexIntentDisambiguationSettings(BaseModel):
    enabled: StrictBool | None = None
    maxDisambiguationIntents: StrictInt | None = None
    customDisambiguationMessage: StrictStr | None = None
