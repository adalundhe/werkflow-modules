from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsIndiaAdditionalInfo(BaseModel):
    pan: StrictStr | None = None
