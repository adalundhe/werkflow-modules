from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsGreeceAdditionalInfo(BaseModel):
    contractingAuthorityCode: StrictStr | None = None
