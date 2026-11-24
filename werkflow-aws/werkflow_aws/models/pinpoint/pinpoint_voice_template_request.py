from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointVoiceTemplateRequest(BaseModel):
    Body: StrictStr | None = None
    DefaultSubstitutions: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    TemplateDescription: StrictStr | None = None
    VoiceId: StrictStr | None = None
