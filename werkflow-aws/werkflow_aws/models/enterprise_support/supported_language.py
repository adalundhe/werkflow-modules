from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SupportedLanguage(BaseModel):
    code: StrictStr | None = None
    language: StrictStr | None = None
    display: StrictStr | None = None
