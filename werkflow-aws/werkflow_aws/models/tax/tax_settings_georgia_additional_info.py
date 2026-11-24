from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsGeorgiaAdditionalInfo(BaseModel):
    personType: StrictStr | None = None
