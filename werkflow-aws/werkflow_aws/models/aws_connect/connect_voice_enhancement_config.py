from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectVoiceEnhancementConfig(BaseModel):
    Channel: StrictStr | None = None
    VoiceEnhancementMode: StrictStr | None = None
