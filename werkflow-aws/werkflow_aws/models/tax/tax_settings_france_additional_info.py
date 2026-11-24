from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsFranceAdditionalInfo(BaseModel):
    sirenNumber: StrictStr | None = None
    eInvoiceRoutingCode: StrictStr | None = None
