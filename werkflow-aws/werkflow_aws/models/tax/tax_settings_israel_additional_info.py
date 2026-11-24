from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsIsraelAdditionalInfo(BaseModel):
    dealerType: StrictStr | None = None
    customerType: StrictStr | None = None
