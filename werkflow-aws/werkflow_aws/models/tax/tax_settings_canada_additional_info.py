from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class TaxSettingsCanadaAdditionalInfo(BaseModel):
    provincialSalesTaxId: StrictStr | None = None
    canadaQuebecSalesTaxNumber: StrictStr | None = None
    canadaRetailSalesTaxNumber: StrictStr | None = None
    isResellerAccount: StrictBool | None = None
