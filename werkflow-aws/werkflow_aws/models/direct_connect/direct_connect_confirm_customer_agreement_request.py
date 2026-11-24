from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectConfirmCustomerAgreementRequest(BaseModel):
    agreementName: StrictStr | None = None
