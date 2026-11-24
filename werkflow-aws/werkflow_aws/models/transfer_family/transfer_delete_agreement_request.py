from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDeleteAgreementRequest(BaseModel):
    AgreementId: StrictStr
    ServerId: StrictStr
