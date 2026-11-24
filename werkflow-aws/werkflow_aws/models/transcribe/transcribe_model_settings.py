from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeModelSettings(BaseModel):
    LanguageModelName: StrictStr | None = None
