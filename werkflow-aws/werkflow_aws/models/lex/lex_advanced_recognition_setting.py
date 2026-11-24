from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexAdvancedRecognitionSetting(BaseModel):
    audioRecognitionStrategy: StrictStr | None = None
