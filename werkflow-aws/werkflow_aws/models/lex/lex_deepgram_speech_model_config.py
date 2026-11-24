from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDeepgramSpeechModelConfig(BaseModel):
    apiTokenSecretArn: StrictStr | None = None
    modelId: StrictStr | None = None
