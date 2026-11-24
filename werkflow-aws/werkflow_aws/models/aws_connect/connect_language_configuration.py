from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectLanguageConfiguration(BaseModel):
    LanguageLocale: StrictStr | None = None
