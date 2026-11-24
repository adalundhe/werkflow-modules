from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsEstoniaAdditionalInfo(BaseModel):
    registryCommercialCode: StrictStr | None = None
