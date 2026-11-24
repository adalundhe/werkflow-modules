from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsGetTaxRegistrationRequest(BaseModel):
    accountId: StrictStr | None = None
