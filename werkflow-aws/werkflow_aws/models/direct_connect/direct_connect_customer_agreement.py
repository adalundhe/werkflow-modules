from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectCustomerAgreement(BaseModel):
    agreementName: StrictStr | None = None
    status: StrictStr | None = None
