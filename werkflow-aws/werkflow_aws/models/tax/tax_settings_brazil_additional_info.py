from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsBrazilAdditionalInfo(BaseModel):
    ccmCode: StrictStr | None = None
    legalNatureCode: StrictStr | None = None
