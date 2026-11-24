from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsDeleteTaxRegistrationRequest(BaseModel):
    accountId: StrictStr | None = None
