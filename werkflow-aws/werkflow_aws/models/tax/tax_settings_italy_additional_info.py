from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsItalyAdditionalInfo(BaseModel):
    sdiAccountId: StrictStr | None = None
    cigNumber: StrictStr | None = None
    cupNumber: StrictStr | None = None
    taxCode: StrictStr | None = None
    customerType: StrictStr | None = None
