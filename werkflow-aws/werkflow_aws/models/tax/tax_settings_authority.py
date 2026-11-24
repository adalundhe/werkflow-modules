from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsAuthority(BaseModel):
    country: StrictStr | None = None
    state: StrictStr | None = None
