from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class TaxSettingsVietnamAdditionalInfo(BaseModel):
    enterpriseIdentificationNumber: StrictStr | None = None
    electronicTransactionCodeNumber: StrictStr | None = None
    paymentVoucherNumber: StrictStr | None = None
    paymentVoucherNumberDate: StrictStr | None = None
    vatCreditMethod: StrictBool | None = None
