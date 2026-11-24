from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointVoiceMessage(BaseModel):
    Body: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    OriginationNumber: StrictStr | None = None
    Substitutions: dict[StrictStr, list[StrictStr]] | None = None
    VoiceId: StrictStr | None = None
