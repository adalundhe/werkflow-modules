from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsBatchDeleteTaxRegistrationError(BaseModel):
    accountId: StrictStr | None = None
    message: StrictStr | None = None
    code: StrictStr | None = None
