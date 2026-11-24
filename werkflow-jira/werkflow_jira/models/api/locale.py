from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Locale(BaseModel):
    locale: StrictStr | None = None
