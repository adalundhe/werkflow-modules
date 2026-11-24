from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsSouthKoreaAdditionalInfo(BaseModel):
    businessRepresentativeName: StrictStr | None = None
    lineOfBusiness: StrictStr | None = None
    itemOfBusiness: StrictStr | None = None
